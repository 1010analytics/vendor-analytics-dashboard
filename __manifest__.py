{
    'name': 'Vendor Analytics Dashboard',
    'version': '1.0',
    'summary': 'An analytics dashboard for vendor management',
    'author': 'Your Name',
    'category': 'Sales',
    'website': 'https://www.example.com',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        'views/vendor_analytics_dashboard.xml',
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
