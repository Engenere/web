# @author Felipe Motter Pereira <felipe@engenere.one>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Web Company Color For Responsive Client",
    "summary": "Integration between Company Color And Responsive",
    "version": "14.0.0.0.0",
    "development_status": "Beta",
    "category": "Website",
    "website": "https://github.com/OCA/web",
    "author": "Engenere, " "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["web_responsive", "web_company_color"],
    "auto_install": True,
    "maintainers": ["felipemotter"],
    "data": ["views/assets.xml"],
    "uninstall_hook": "uninstall_hook",
    "post_init_hook": "post_init_hook",
}
