# @author Felipe Motter Pereira <felipe@engenere.one>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models

from .assetsbundle import AssetsBundleCompanyColor


class QWeb(models.AbstractModel):
    _inherit = "ir.qweb"

    def _get_asset_content(self, xmlid, options):
        """Handle 'special' web_company_color xmlid"""
        if xmlid == "web_company_color_responsive.web_responsive_assets":
            asset = AssetsBundleCompanyColor(xmlid, [], env=self.env)
            return ([], [asset.get_company_color_asset_node()])
        return super()._get_asset_content(xmlid, options)
