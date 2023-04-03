# -*- coding: utf-8 -*-
from odoo import fields, models

class  Request(models.Model):
    _name = 'workspace.request.lines'
    _description = 'Request'
    name = fields.Char(string='Name')
    http_method= fields.Selection([
        ('get','GET'),
        ('post','POST'),
        ('put','PUT'),
        ('delete','DELETE'),
        ],
        string='HTTP Method',
        default='get'
    )
    url = fields.Char(string='Url')
    nbr_request=fields.Integer(string='Number of requests')
    workspace_id=fields.Many2one("workspace",string="Appointment")
