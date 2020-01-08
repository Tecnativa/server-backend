# Copyright 2020 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SageLcMixin(models.AbstractModel):
    """ It provides the unique key for sqlserver table. """

    _inherit = 'dbsource.external.mixin'
    _name = 'dbsource.sage.lc.mixin'

    sagelc_key = fields.Char(copy=False)
