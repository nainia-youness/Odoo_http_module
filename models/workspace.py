# -*- coding: utf-8 -*-
from odoo import fields, models

class  Workspace(models.Model):
    _name = 'workspace'
    _description = 'Your workspace'
    name = fields.Char(string='Name')
