# -*- coding: utf-8 -*-
{
    'name': "vcls-contact",

    'summary': """
        VCLS custom contact module
        """,

    'description': """
    """,

    'author': "VCLS",
    'website': "https://voisinconsulting.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
        'survey',
        ],

    # always loaded
    'data': [

        ### CONFIGURATION DATA ###
        'data/res.partner.category.csv',
        'data/ir.config_parameter.csv',
        'data/client.activity.csv',
        'data/client.product.csv',
        #'data/partner.seniority.csv',
        #'data/partner.functional.focus.csv',
        
        ### SECURITY ###
        'security/vcls_groups.xml',
        'security/ir.model.access.csv',
        'security/contact_rules.xml',
        
        ### VIEWS ###
        'views/dropdown_views.xml',
        'views/contact_views.xml',

        ### MENUS ###
        'views/contact_menu.xml',

        ### ACTIONS ###
        'actions/contact_server_action.xml',
        ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}