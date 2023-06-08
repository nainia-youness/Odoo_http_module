# -*- coding: utf-8 -*-
from odoo import fields, models

class  Workspace(models.Model):
    _name = 'workspace'
    _description = 'Your workspace'
    _rec_name = 'name'
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    request_line_ids=fields.One2many('workspace.request.lines',"workspace_id",string="Request Lines")