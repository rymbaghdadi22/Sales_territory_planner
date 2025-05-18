from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date

class CustomerVisit(models.Model):
    _name = 'sales.customer.visit'
    _description = 'Customer Visit'

    name = fields.Char(string='Visit Reference', required=True, default=lambda self: 'New')
    customer_id = fields.Many2one('res.partner', string='Customer', domain=[('customer_rank', '>', 0)], required=True)
    territory_id = fields.Many2one('sales.territory', string='Territory')
    visit_date = fields.Date(string='Visit Date', required=True, default=fields.Date.context_today)
    sales_person_id = fields.Many2one('res.users', string='Sales Person', required=True)
    check_in_time = fields.Datetime(string='Check-In Time')
    feedback = fields.Text(string='Customer Feedback')
    inventory_status = fields.Text(string='Inventory Observations')
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('checked_in', 'Checked In'),
        ('done', 'Completed')
    ], string='Status', default='scheduled')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('sales.customer.visit') or 'New'
        return super().create(vals)

    def action_check_in(self):
        for record in self:
            if record.state != 'scheduled':
                raise UserError("Only scheduled visits can be checked in.")
            record.check_in_time = fields.Datetime.now()
            record.state = 'checked_in'

    def action_mark_done(self):
        for record in self:
            if record.state != 'checked_in':
                raise UserError("Only checked-in visits can be marked as done.")
            record.state = 'done'
