

{
    'name': 'Hide Activity Log for User',
    'description': """This Module Use to Hide Activity Log for User""",
    "version": "14.0.1.0.0",
    "category": "tools",
    'author': 'RASHAD ALKHAWLANI - SMART BUSINESS TECH ',
    'website': 'http://www.smart-bt.com',
    'depends': ['base','web','sale'],
    'data': [
        'templates/webclient.xml',
        'views/res_users.xml',
        'views/templates.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
