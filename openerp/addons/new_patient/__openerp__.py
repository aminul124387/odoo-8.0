{
    'name': 'New Patient',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Restaurant extensions for the Point of Sale ',
    'description': """

=======================

This module adds several restaurant features to the Point of Sale:
- Bill Printing: Allows you to print a receipt before the order is paid
- Bill Splitting: Allows you to split an order into different orders
- Kitchen Order Printing: allows you to print orders updates to kitchen or bar printers

""",
    'author': 'OpenERP SA',
    'depends': ['point_of_sale'],
    'website': 'https://www.odoo.com/page/point-of-sale',
    'data': [
        'views/add_patient.xml',

    ],
    'qweb':[
        'static/src/xml/multiprint.xml',
        'static/src/xml/splitbill.xml',
        'static/src/xml/printbill.xml',
    ],
    'installable': True,
    'auto_install': False,
}
