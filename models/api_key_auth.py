from odoo import fields, models

class  APIKeyAuthorization(models.Model):
    _name = 'api_key_auth'
    _description = 'api_key_auth'
    _inherit=['authorization']
    key = fields.Char(string='Key')
    value = fields.Char(string='Value')
