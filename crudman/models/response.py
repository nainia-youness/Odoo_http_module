# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Response(models.Model):
    _name = 'request.response'
    _description = 'Response'
    request_date= fields.Datetime(string='Request date',default=fields.Datetime.now)
    name = fields.Char(string='Name')
    response_time = fields.Float(string='Response time')
    size = fields.Float(string='Size')
    body_content=fields.Text(string='Body content')
    status_code = fields.Integer(related='http_status_id.code')
    request_id=fields.Many2one('workspace.request.lines',string='Request')
    http_status_id=fields.Many2one('response.httpstatus',string='Http status')
    header_line_ids=fields.One2many('request.header.lines',"response_id",string="Headers")
    cookie_line_ids=fields.One2many('request.cookie.lines',"response_id",string="Cookies")


    @api.model
    def create(self,vals):
        vals['name']=self.env['ir.sequence'].next_by_code('request.response')
        return super(Response,self).create(vals)