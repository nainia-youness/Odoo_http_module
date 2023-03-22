# -*- coding: utf-8 -*-
from odoo import fields, models

class  Query(models.Model):
    _name = 'query'
    _description = 'query parameter'
    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
    description = fields.Char(string='Description')
    active=fields.Boolean(string='Active',default=True)
    request_id=fields.Many2one('request',string='Request')
