# -*- coding: utf-8 -*-
from odoo import fields, models

class Connection(models.Model):
    _name = 'connection'
    _description = 'Http connection'
    url = fields.Char(string='URL',help="url of the request")
