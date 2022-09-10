from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResPartnerVisit(models.Model):
    _name = 'customer.visit'

    def _default_user_id(self):
        if not self.user_id:
            return self.env.user
        return False


    def _default_visit_ids(self):
        print('_default_customer_id')
        if self._context['active_model'] == 'res.partner' and not self.visit_ids:
            customer = self.env['res.partner'].browse(self._context['active_id'])
            if customer:
                return customer
            else:
                return False
        else:
            return False

    visit_ids = fields.Many2one("res.partner", string="Customer",)
    display_name = fields.Char(compute='_compute_display_name')

    visit_date = fields.Date(string="Visit Date",default=fields.Date.today())
    assigned_by = fields.Many2one(comodel_name="res.users", string="Assigned by", default=_default_user_id, )
    visit_type = fields.Selection(
        selection=[
            ('1','New Order'),
            ('2', 'Visit'),
            ('3','Collection'),
            ('4','Return'),
            ('5','Delivery'),
            ('6', 'Direct')
        ], string='Visit Purpose', default='6')
    state = fields.Selection(
        selection=[
            ('draft','Draft'),
            ('assigned','Assigned'),
            ('waiting','Waiting'),
            ('done', 'Done')
        ], default='draft', string='Visit State',tracking=1, track_visibility='onchange')

    user_id = fields.Many2one(comodel_name="res.users",
                              string="Salesperson",
                              default=_default_user_id,
                              tracking=1,
                              domain=lambda self: [("groups_id","=",
                                                    self.env.ref("sales_team.group_sale_salesman").id)
                                                   ]
                              )
    meeting_person_name = fields.Char(string="Person Name",  required=False, )
    meeting_person_phone = fields.Char(string="Person Phone",  required=False, )
    reason_visit = fields.Char(string="Visit Reason",  required=False, )
    result_visit = fields.Char(string="Visit Result",  required=False, )
    is_assigned_next_visit = fields.Boolean(string="Is assigned Next Visit Date?")
    next_visit = fields.Date(string="Next Visit Date", required=False, )
    latitude = fields.Float(
        "Visit Latitude", digits="Location"
    )
    longitude = fields.Float(
        "Visit Longitude", digits="Location"
    )
    street = fields.Char(string='Address')
    map = fields.Char(string='map')

    @api.onchange('visit_ids')
    def _onchange_customer(self):
        if self.visit_ids:
            if not self.latitude:
                print(self.visit_ids.partner_latitude)
                self.write({'latitude':self.visit_ids.partner_latitude})
            if not self.longitude:
                self.write({'longitude': self.visit_ids.partner_longitude})

    def button_done(self):
        self.write({"state": "done"})

    def button_waiting(self):
        self.write({"state": "waiting"})

    def button_draft(self):
        self.write({"state": "draft", "user_id": False})

    def button_assigned(self):
        if not self.user_id:
            raise ValidationError("Please Select Salesperson, Without Salesperson Visit State Can not be Assigned")
        self.write({"state": "assigned"})

    @api.depends('visit_ids')
    def _compute_display_name(self):
        for cat in self:
            if cat.visit_ids:
                cat.display_name = cat.visit_ids.display_name
            else:
                cat.display_name = _('New Visit')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    visits_ids = fields.One2many("customer.visit", "visit_ids", string="Customer Visits", required=False, )


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    visits_ids = fields.One2many("customer.visit", compute='_compute_visits_ids', string="Customer Visits", )

    @api.onchange("partner_id")
    def onchange_partner_id_visits_ids(self):
        if self.partner_id.visits_ids:
            self.visits_ids = self.partner_id.visits_ids

    def _compute_visits_ids(self):
        if self.partner_id.visits_ids:
            self.visits_ids = self.partner_id.visits_ids
        else:
            self.visits_ids = False
