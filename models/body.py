# -*- coding: utf-8 -*-
from odoo import fields, models

class  Body(models.Model):
    _name = 'body'
    _description = 'Body'
    request_id=fields.Many2one('request',string='Request')
    response_id=fields.Many2one('response',string='Request')
    