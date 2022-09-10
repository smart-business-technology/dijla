
{
    "name": "Filter Partners on Sales and Purchases",
    "summary": """Show Customers Only on Sales & Show Suppliers Only on Purchases""",
    "version": "14.0.1.0.0",
    "category": "tools",
    'website': 'https://www.smart-bt.com',
    'author': 'RASHAD ALKHAWLANI - SMART BUSINESS TECH ',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "data": ["views/partner_view.xml"],
    "depends": ["base", "sale", "account", "purchase", "customer_approved"],
}
