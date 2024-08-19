{
    'name': 'API PORTAL',
    'version': '1.0',
    'author': 'MUHAIMENUL',
    'category': 'Technical',
    'depends': ['base', 'mail', 'uom', "sale", "hr"],

    'description': """
    """,
    'data': [
                'security/ir.model.access.csv',
                'views/portal_data_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
