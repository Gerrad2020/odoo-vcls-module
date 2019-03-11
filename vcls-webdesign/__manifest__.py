# -*- coding: utf-8 -*-
{
    'name': 'VCLS webdesign',
    'summary': "VCLS webdesign",
    'version': '0.1',
    'author': "Odoo",
    'category': 'Website',
    'depends': ['website','website_form_editor','documents'],
    'data': [

        #data
        'data/documents.xml',

        #frontend
        'views/assets.xml',
        'views/snippets.xml',
        'views/documents.xml',

    ],
    'auto_install': True,
    'installable': True,
}
