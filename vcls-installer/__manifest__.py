# -*- coding: utf-8 -*-
{
    'name': "vcls-installer",

    'summary': """
        This module install every other VCLS modules in order to avoid conflicts.
        """,

    'description': """
    """,

    'author': "VCLS",
    'website': "http://www.voisinconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                # install contacts before
                'vcls-hr',
                'vcls-helpdesk',
                'vcls-contact',
                'vcls-crm',
                'vcls-interfaces',
                'vcls-project',
                'vcls-theme'
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}