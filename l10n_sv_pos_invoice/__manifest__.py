# -*- coding: utf-8 -*-
{
    'name': 'El Salvador - POS Types of DTE Document',
    'version': '18.0.1.0.0',
    'summary': 'Generación automática de JSON DTE desde POS con asignación de tipo de documento',
    'description': """
Este módulo implementa los tipos de documento según el catálogo CAT_002_Tipo_de_Documento
de la Dirección General de Impuestos Internos de El Salvador.
""",
    'author': 'miliky',
    'maintainer': 'José Emilio Flores Meléndez',
    'website': 'https://github.com/miliky/odoo18',
    'category': 'Point of Sale',
    'license': 'LGPL-3',
    'images': ['static/description/banner.jpg'],
    'price': 0.0,
    'currency': 'USD',
    'depends': ["point_of_sale", "l10n_sv_document_type", "l10n_sv_edi_json"],
    'data': [
        'views/account_move_views.xml',
        'security/ir.model.access.csv',
        'views/l10n_sv_establishment_views.xml',
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
