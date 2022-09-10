from odoo import api, fields, models


class Users(models.Model):
    _inherit = "res.users"

    assigned_journal_id = fields.Many2one(
        "account.journal",
        string="Sales Journal",
        domain="[('type', 'in', ('cash','bank'))]",
        help="Specifying Sales Journal to User.",
    )
