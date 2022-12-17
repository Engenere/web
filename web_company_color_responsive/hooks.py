# @author Felipe Motter Pereira <felipe@engenere.one>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import SUPERUSER_ID, api

from .models.res_company import RESPONSIVE_URL_BASE


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["ir.attachment"].search(
        [("url", "=like", "%s%%" % RESPONSIVE_URL_BASE)]
    ).unlink()


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["res.company"].search([]).scss_create_or_update_attachment()
