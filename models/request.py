# -*- coding: utf-8 -*-
from odoo import api,fields, models
from urllib.parse import urlparse,parse_qs
import requests
from datetime import date

class  Request(models.Model):
    _name = 'workspace.request.lines'
    _description = 'Request'
    name = fields.Char(string='Name')
    http_method= fields.Selection([
        ('get','GET'),
        ('post','POST'),
        ('put','PUT'),
        ('delete','DELETE'),
        ],
        string='HTTP Method',
        default='get'
    )
    url = fields.Char(string='Url')
    nbr_request=fields.Integer(string='Number of requests',default=1)
    auth_type= fields.Selection([
         ('no_auth','No Auth'),
         #('api_key_auth','API Key'),
         ('basic_auth','Basic Auth'),
         #('bearer_token','Bearer Token'),
         ],
         string='Authentication type',
         default='no_auth'
    )
    body_type= fields.Selection([
        ('raw','Raw'),
        ],
        string='Body type',
        default='raw'
    )
    body_format=fields.Selection([
        ('text','Text'),
        ('json','Json'),
        ('html','HTML'),
        ('xml','XML'),
        ],
        string='Body format',
        default='text'
    )
    body_content=fields.Text(string='Body content')
    is_timeout = fields.Boolean(string="Is timeout",default=False)
    timeout= fields.Float('Timeout',default=0.01)
    body_is_pretty= fields.Boolean(string="body Pretty",default=False)
    workspace_id=fields.Many2one("workspace",string="Appointment")
    response_line_ids = fields.One2many('request.response', "request_id", string="Responses")
    query_line_ids=fields.One2many('request.query.lines',"request_id",string="Query params")
    header_line_ids=fields.One2many('request.header.lines',"request_id",string="Headers")
    cookie_line_ids=fields.One2many('request.cookie.lines',"request_id",string="Cookies")

    def get_query_params(self,url):
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query)

    def get_dictionnary(self,records):
        result = {}
        for r in records:
            result[r.key] = r.value
        return result

    def action_send_request(self):
        if(self.nbr_request<=0): return
        for _ in range(self.nbr_request):
            params = self.env['request.query.lines'].search([('request_id', '=', self.id)])
            cookies = self.env['request.cookie.lines'].search([('request_id', '=', self.id)])
            headers = self.env['request.header.lines'].search([('request_id', '=', self.id)])
            params_dict, cookies_dict, headers_dict, timeout = {}, {}, {}, None
            if (self.is_timeout):
                timeout = self.timeout
            if (params): params_dict = self.get_dictionnary(params)
            if (cookies): cookies_dict = self.get_dictionnary(cookies)
            if (headers): headers_dict = self.get_dictionnary(headers)
            # send the request
            if (self.http_method == 'get'):
                try:
                    api_res = requests.get(self.url, params=params_dict, cookies=cookies_dict, headers=headers_dict,
                                           timeout=timeout)
                except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as error:
                    return self.action_notification("Timeout Error",'warning')
            elif (self.http_method == 'post'):
                try:
                    api_res = requests.post(self.url, data=self.body_content, params=params_dict, cookies=cookies_dict,
                                            headers=headers_dict,
                                            timeout=timeout)
                except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as error:
                    return self.action_notification("Timeout Error",'warning')
            elif (self.http_method == 'put'):
                try:
                    api_res = requests.put(self.url, data=self.body_content, params=params_dict, cookies=cookies_dict,
                                            headers=headers_dict,
                                            timeout=timeout)
                except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as error:
                    return self.action_notification("Timeout Error",'warning')
            elif (self.http_method == 'delete'):
                try:
                    api_res = requests.delete(self.url, params=params_dict, cookies=cookies_dict,
                                            headers=headers_dict,
                                            timeout=timeout)
                except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as error:
                    return self.action_notification("Timeout Error",'warning')
            else:
                return

            record = {
                'body_content': api_res.content,
                'request_id': self.id,
                'size': len(api_res.content) + len(api_res.headers),
                'response_time': api_res.elapsed.total_seconds() * 1000
            }
            status_code = self.env['response.httpstatus'].search([('code', '=', api_res.status_code)])
            if (status_code):
                record['http_status_id'] = status_code.id
            else:
                new_status_code = self.env['http_status_id'].create({'code': api_res.status_code, 'name': 'Unassigned'})
                record['http_status_id'] = new_status_code.id
            try:
                response = self.env['request.response'].create(record)
            except:
                record['body_content'] = str(record['body_content']).encode()
                response = self.env['request.response'].create(record)
            # add headers to response
            for key, value in api_res.headers.items():
                self.env['request.header.lines'].create({'response_id': response.id, 'key': key, 'value': value})
            # add cookies to response
            for key, value in api_res.cookies.items():
                self.env['request.cookie.lines'].create({'response_id': response.id, 'key': key, 'value': value})
            print(response)

    def action_notification(self,message,type):
        return {
            'type':'ir.actions.client',
            'tag':'display_notification',
            'params':{
                'message':message,
                'type':type,
                'sticky':False
            }
        }