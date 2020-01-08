# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Base External Dbsource MsSql SAGE Logic Class',
    'summary': 'Import data from SAGE Logic Class ERP',
    'version': '12.0.1.0.0',
    'development_status': 'Alpha',
    'category': 'Tools',
    'website': 'https://github.com/OCA/server-backend',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'installable': True,
    'external_dependencies': {
        'python': [
            'sqlalchemy',
            'pymssql',
        ],
    },
    'depends': [
        'base_external_dbsource_importer',
        'base_external_dbsource_mssql',
        'account_payment_partner',
        'l10n_es_partner',
        'account_payment_term_extension',
    ],
    'data': [
        'data/base_external_dbsource.xml',
        'views/base_external_dbsource_view.xml',
    ],
}
