# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.base_external_dbsource_importer.models.base_external_dbsource\
    import BaseExternalModelImporter

from odoo import models
from odoo.tools import ormcache

_logger = logging.getLogger(__name__)


class BaseExternalModelImporterSageLc(BaseExternalModelImporter):
    _external_key = 'sagelc_key'

    def execute_query(self, sql, params, metadata=True):
        return self.dbsource.execute_mssql(sql, params, metadata)


class BaseExternalDbsourceSage200(models.Model):
    """ It provides logic for connection to a MsSQL data source. """

    _inherit = "base.external.dbsource"

    def _prepare_payment_mode_data_sage(self, row, payment_method):
        return {
            'sagelc_key': '{}'.format(row.N_Reglement),
            'name': row.R_Intitule,
            'bank_account_link': 'variable',
            'payment_method_id': payment_method.id,
        }

    def action_import_payment_mode_sage(self):
        importer = BaseExternalModelImporterSageLc(dbsource=self)
        payment_method = self.env.ref(
            'account.account_payment_method_manual_out')
        fields = """
            DISTINCT(N_Reglement) AS N_Reglement,
            P_REGLEMENT.R_Intitule AS R_Intitule
        """
        table_name = """
            F_REGLEMENTT INNER JOIN P_REGLEMENT ON
            F_REGLEMENTT.N_Reglement = P_REGLEMENT.cbIndice
        """
        where = "WHERE CT_Num like 'P%'"

        ext_records, records, records_dic = importer.load_data(
            'account.payment.mode', table_name=table_name,
            fields=fields, where=where)
        for fds_rec in ext_records:
            vals = self._prepare_payment_mode_data_sage(
                fds_rec, payment_method)
            importer.upsert(vals['sagelc_key'], records, records_dic, vals)
