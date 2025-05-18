{
    'name': 'Sales Territory Planner',
    'license': 'LGPL-3',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage sales territories and assign them to salespersons',
    'description': """
        Track sales territories, zones, and visit schedules.
    """,
    'author': 'Rym Baghdadi',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/visit_sequence.xml',
        'views/sales_territory_views.xml',
        'views/customer_visit_views.xml', 
        'views/customer_inventory_views.xml',
        'views/dashboard_views.xml',
        'views/menu.xml',  
    ],
    'assets': {
        'web.assets_backend': [
            'sales_territory_planner/static/src/js/sales_dashboard.js',
            'sales_territory_planner/static/src/xml/sales_dashboard.xml',
            'sales_territory_planner/static/src/scss/sales_dashboard.scss',
        ],
    },
    'installable': True,
    'application': True,
}
