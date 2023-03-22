# -*- coding: utf-8 -*-
from odoo import fields, models

class  Cookie(models.Model):
    _name = 'cookie'
    _description = 'Request Cookie'
    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    description = fields.Char(string='Description')
    active=fields.Boolean(string='Active',default=True)
    request_id=fields.Many2one('request',string='Request')
    response_id=fields.Many2one('response',string='Request')