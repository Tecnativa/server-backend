# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountAccount(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = ['account.account', 'dbsource.sage.lc.mixin']
    _name = 'account.account'


class AccountAnalyticAccount(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = ['account.analytic.account', 'dbsource.sage.lc.mixin']
    _name = 'account.analytic.account'


class AccountJournal(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = ['account.journal', 'dbsource.sage.lc.mixin']
    _name = 'account.journal'


class AccountMove(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = ['account.move', 'dbsource.sage.lc.mixin']
    _name = 'account.move'

    sagelc_key = fields.Char(index=True)


class AccountMoveLine(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = ['account.move.line', 'dbsource.sage.lc.mixin']
    _name = 'account.move.line'

    sage200_reconcile_link = fields.Integer(index=True)
    sage200_reconcile_link2 = fields.Char(index=True)
