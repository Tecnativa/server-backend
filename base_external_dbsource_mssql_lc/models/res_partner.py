# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class ResPartner(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = ['res.partner', 'dbsource.sage.lc.mixin']
    _name = 'res.partner'


class ResPartnerBank(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = ['res.partner.bank', 'dbsource.sage.lc.mixin']
    _name = 'res.partner.bank'

    _sql_constraints = [
        ('unique_number',
         'unique(sanitized_acc_number, company_id, partner_id)',
         'Account Number must be unique'),
    ]
