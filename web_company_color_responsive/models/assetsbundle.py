# @author Felipe Motter Pereira <felipe@engenere.one>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo.addons.base.models.assetsbundle import AssetsBundle, ScssStylesheetAsset


class AssetsBundleCompanyColor(AssetsBundle):
    def get_company_color_asset_node(self):
        """Process the user active company scss and returns the node to inject"""
        company_id = self.env["res.company"].browse(
            self.env.context.get("active_company_id", 0)
        )
        asset = ScssStylesheetAsset(self, url=company_id.scss_get_resp_url())
        compiled = self.compile_css(asset.compile, asset.get_source())
        return ("style", {}, compiled)
