# Copyright 2025 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class BaseModel(models.AbstractModel):
    _inherit = "base"
    # _phone_fields
    _sanitized_fields = []
    _sanitized_tokens = ""
