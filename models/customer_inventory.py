from odoo import models, fields, api

class CustomerInventory(models.Model):
    _name = 'customer.inventory'
    _description = 'Inventory at Customer Locations'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    current_stock = fields.Float(string='Current Stock', default=0)
    min_stock_level = fields.Float(string='Minimum Stock Level', help="Alert when stock goes below this")
    last_updated = fields.Datetime(string='Last Updated', default=fields.Datetime.now)
    visit_id = fields.Many2one('sales.customer.visit', string='Related Visit')

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record.check_stock_alert()
        return record

    def write(self, vals):
        res = super().write(vals)
        if 'current_stock' in vals:
            self.check_stock_alert()
        return res

    def check_stock_alert(self):
        for record in self:
            if record.current_stock < record.min_stock_level:
                self.env['mail.message'].create({
                    'body': f"Low stock alert for {record.product_id.name} at {record.customer_id.name}",
                    'subject': "Low Stock Alert",
                    'partner_ids': [(4, record.customer_id.id)],
                    'model': 'customer.inventory',
                    'res_id': record.id,
                })
