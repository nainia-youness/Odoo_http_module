# -*- coding: utf-8 -*-
from odoo import fields, models

class  Header(models.Model):
    _name = 'request.header.lines'
    _description = 'Request header'
    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    description = fields.Char(string='Description')
    active=fields.Boolean(string='Active',default=True)
    request_id=fields.Many2one('workspace.request.lines',string='Request')