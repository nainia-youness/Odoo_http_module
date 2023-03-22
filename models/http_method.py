# -*- coding: utf-8 -*-
from odoo import fields, models

class  HttpMethod(models.Model):
    _name = 'http_method'
    _description = 'Http method'
    code = fields.Integer(string='Code')
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    