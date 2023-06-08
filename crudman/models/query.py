# -*- coding: utf-8 -*-
from odoo import fields, models

class  Query(models.Model):
    _name = 'request.query.lines'
    _description = 'query parameter'
    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    description = fields.Char(string='Description')
    active=fields.Boolean(string='Active',default=True)
    request_id=fields.Many2one('workspace.request.lines',string='Request')
    response_id = fields.Many2one('request.response', string='Response')
