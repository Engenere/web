# @author Felipe Motter Pereira <felipe@engenere.one>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
import base64

from odoo import models

RESPONSIVE_URL_BASE = "/web_company_color_responsive/static/src/scss/"
RESP_URL_SCSS_GEN_TEMPLATE = (
    RESPONSIVE_URL_BASE + "responsive_custom_colors.%d.gen.scss"
)


class ResCompany(models.Model):
    _inherit = "res.company"

    RESP_SCSS_TEMPLATE = """
    .o_menu_apps {
      .dropdown-menu {
        background:
            url("/web_responsive/static/src/scss/web_responsive.scss"),
            linear-gradient(
                to bottom,%(color_navbar_bg)s,
                desaturate(lighten(%(color_navbar_bg)s, 20%%), 15)
            );
      }
    }
    """

    def unlink(self):
        IrAttachmentObj = self.env["ir.attachment"]
        for record in self:
            IrAttachmentObj.sudo().search(
                [
                    ("url", "=", record.scss_get_resp_url()),
                    ("company_id", "=", record.id),
                ]
            ).sudo().unlink()
        return super().unlink()

    def _scss_generate_resp_content(self):
        self.ensure_one()
        # ir.attachment need files with content to work
        if not self.company_colors:
            return "// No Web Company Color SCSS Content\n"
        return self.RESP_SCSS_TEMPLATE % self._scss_get_sanitized_values()

    def scss_get_resp_url(self):
        self.ensure_one()
        return RESP_URL_SCSS_GEN_TEMPLATE % self.id

    def scss_create_or_update_attachment(self):
        super().scss_create_or_update_attachment()
        IrAttachmentObj = self.env["ir.attachment"]
        for record in self:
            datas = base64.b64encode(
                record._scss_generate_resp_content().encode("utf-8")
            )
            custom_url = record.scss_get_resp_url()
            custom_attachment = IrAttachmentObj.sudo().search(
                [("url", "=", custom_url), ("company_id", "=", record.id)]
            )
            values = {
                "datas": datas,
                "db_datas": datas,
                "url": custom_url,
                "name": custom_url,
                "company_id": record.id,
            }
            if custom_attachment:
                custom_attachment.sudo().write(values)
            else:
                values.update({"type": "binary", "mimetype": "text/scss"})
                IrAttachmentObj.sudo().create(values)
        self.env["ir.qweb"].sudo().clear_caches()
