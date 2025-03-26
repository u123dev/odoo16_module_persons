{
    'name': 'Persons',
    'version': '1.0',
    'summary': 'Module to manage persons',
    'description': "Manage Persons: List, Add, etc.",
    'category': 'Website',
    'author': 'u123dev',
    'depends': ['base', 'website'],
    'assets': {
        'web.assets_frontend': [
            'persons/static/src/css/style.css',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/person_views.xml',
        'views/menu.xml',
        'views/persons_template.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}