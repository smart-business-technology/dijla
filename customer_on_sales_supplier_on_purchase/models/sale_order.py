
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', '&','&', ('customer_rank','>',0), ('company_id', '=', False), ('state','=','approved'),'&','&', ('customer_rank','>',0), ('company_id', '=', company_id),('state','=','approved')]")
