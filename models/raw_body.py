from odoo import fields, models


class RawBody(models.Model):
    _inherit = ['body']

    content=fields.Text(string='Content')
    data_format=fields.Selection([
        ('text','Text'),
        ('json','Json'),
        ('html','HTML'),
        ('xml','XML'),
        ],
        string='Data format',
        default='text'
    )
    is_pretty= fields.Boolean(string="Pretty",default=False)