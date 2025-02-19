{
    'name': 'Person Management',
    'version': '16.0.1.0.0',
    'category': 'Website',
    'summary': 'Manage persons with website integration',
    'description': '''
        Module for managing persons, their details, and displaying them on the website.
    ''',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/person_views.xml',
        'views/website_templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
