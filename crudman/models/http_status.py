# -*- coding: utf-8 -*-
from odoo import fields, models

class  HttpStatus(models.Model):
    _name = 'response.httpstatus'
    _description = 'Response http status'
    code = fields.Integer(string='Code')
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')