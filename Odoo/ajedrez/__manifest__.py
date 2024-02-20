# -*- coding: utf-8 -*-
{
    'name': "Ajedrez",
    'application': True,
    'installable': True,
    'summary': """
        Módulo ajedrez de Alberto Rodríguez Pérez
        Asignatura SGE 23-24""",

    'description': """
        Módulo de gestión de partidas de ajedrez con relaciones con jugadores y editoriales, también creados
    """,

    'author': "Alberto RP",
    'website': "https://github.com/0zaRu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/grupos.xml',
        'security/ir.model.access.csv',
        'views/vistas.xml',
        'views/templates.xml',
        'demo/demo.xml',
        'reports/informes.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
