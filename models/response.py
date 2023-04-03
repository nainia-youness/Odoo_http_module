# -*- coding: utf-8 -*-
from odoo import fields, models

class  Response(models.Model):
    _name = 'request.response'
    _description = 'Response'
    name = fields.Char(string='Name')
    response_time = fields.Datetime(string='Response time')
    size = fields.Float(string='Size')
    request_id=fields.Many2one('workspace.request.lines',string='Request')
    #http_method_id=fields.Many2one('http_method',string='Http method')
    
