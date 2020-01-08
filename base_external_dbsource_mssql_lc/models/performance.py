# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    date = fields.Date(index=True)


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    date = fields.Date(index=True)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    date_invoice = fields.Date(index=True)
    number = fields.Char(index=True)
