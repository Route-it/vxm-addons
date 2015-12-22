# -*- coding: utf-8 -*-
{
    'name': "Gestión de turnos",

    'summary': """
        Gestión de turnos para canchas de fútbol
        """,

    'description': """
        Con este módulo se pueden gestionar los turnos de canchas de fútblo, socios para alquiler, historial de pagos, cuentas corrientes y scoring de clientes
    """,

    'author': "Route IT",
    'website': "http://www.routeit.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'view/turns.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}