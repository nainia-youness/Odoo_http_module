# -*- coding: utf-8 -*-
from odoo import fields, models

class  Authorization(models.Model):
    _name = 'authorization'
    _description = 'Authorization'
    request_id=fields.Many2one('request',string='Request')
    