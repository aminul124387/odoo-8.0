{
    'name': 'Investigation Form',
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
        'add_bill_view.xml',
        'bill_register_line_view.xml',
        'bill_register_view.xml',
        'report/bill_report_menu.xml',
        'report/report_bil_register.xml',
        'payment/bill_register_payment_view.xml',
        'investigation_payment/investigation_payment_view.xml'

    ],
    'qweb':[
        'static/src/xml/multiprint.xml',
        'static/src/xml/splitbill.xml',
        'static/src/xml/printbill.xml',
    ],
    'installable': True,
    'auto_install': False,
}
