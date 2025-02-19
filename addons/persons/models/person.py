from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date

class Person(models.Model):
    _name = "person"
    _description = "Person"

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    full_name = fields.Char(compute="_compute_full_name", store=True)
    birthday = fields.Date()
    age = fields.Integer(compute="_compute_age", store=True)
    sex = fields.Selection([("male", "Male"), ("female", "Female"), ("non-binary", "Non-Binary")])
    company_id = fields.Many2one("res.company", required=True, default=lambda self: self.env.company)

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.first_name} {record.last_name}"

    @api.depends("birthday")
    def _compute_age(self):
        today = date.today()
        for record in self:
            record.age = relativedelta(today, record.birthday).years if record.birthday else 0
