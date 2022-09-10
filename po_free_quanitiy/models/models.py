from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    free_qty = fields.Float(string='Free Quantity')

    # if setting bill qty (Received quantities)
    # def _prepare_account_move_line(self, move=False):
    #     self.ensure_one()
    #     res = super(PurchaseOrderLine,self)._prepare_account_move_line(move)
    #     if self.free_qty > 0:
    #         res.update({
    #             'quantity': self.qty_to_invoice - self.free_qty,
    #         })
    #     return res
    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        self.ensure_one()
        print('_prepare_stock_move_vals')
        res = super(PurchaseOrderLine,self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        if self.free_qty > 0:
            res.update({
                'product_uom_qty': self.product_uom_qty + self.free_qty,
            })
        return res

