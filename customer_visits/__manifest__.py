
{
    "name": "Customer Visits",
    "summary": "Customer Visits",
    "version": "14.0.1.0.0",
    "category": "sales",
    "author": 'RASHAD ALKHAWLANI - SMART BUSINESS TECH ',
    'website': 'https://www.smart-bt.com',
    'license': 'AGPL-3',
    "depends": ["base", "sale","crm"],
    "qweb": ['static/src/xml/openstreetmap_visits_template.xml'],
    "data": [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/res_partners.xml",
        "views/views.xml",
        "views/crm_lead_visits.xml"

    ],
    "application": False,
    "auto_install": False,
    "installable": True,
}
