from odoo import api, fields, models


class Users(models.Model):
    _inherit = "res.users"

    assigned_warehouse_id = fields.Many2one(
        "stock.warehouse",
        string="Warehouse",
        domain="[('company_id', '=', company_id)]",
        help="Specifying Warehouse to User.",
    )

    def _get_default_warehouse_id(self):
        if self.env.user.assigned_warehouse_id:
            return self.env.user.assigned_warehouse_id
        else:
            return super(Users,self)._get_default_warehouse_id()
