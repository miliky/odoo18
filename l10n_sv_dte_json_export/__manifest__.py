# -*- coding: utf-8 -*-
{
    'name': 'El Salvador - Invoice Attachment Export',
    'version': '18.0.1.0.1',
    'summary': 'Permite descargar todos los archivos adjuntos',
    'description': """
Permite descargar todos los archivos adjuntos de facturas, incluyendo JSON FSSE
""",
    'author': 'miliky',
    'maintainer': 'José Emilio Flores Meléndez',
    'website': 'https://github.com/miliky/odoo18',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'images': ['static/description/banner.jpg'],
    'price': 0.0,
    'currency': 'USD',
    'depends': ['account'],
    'data': [
        "views/invoice_attachment_wizard_view.xml",
        "views/account_move_view.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}