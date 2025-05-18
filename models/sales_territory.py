from odoo import models, fields

class SalesTerritory(models.Model):
    _name = 'sales.territory'
    _description = 'Sales Territory'

    name = fields.Char(string='Territory Name', required=True)
    zone = fields.Char(string='Zone')
    sales_person_id = fields.Many2one('res.users', string='Sales Person')
    visit_day = fields.Selection([
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ], string='Visit Day')
    is_active = fields.Boolean(string='Active', default=True)