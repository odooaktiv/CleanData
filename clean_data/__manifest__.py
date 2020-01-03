# -*- coding: utf-8 -*-
{
    'name': "Mass Clean/Remove/Delete Data (Bulk Data/Records Cleaner)",
    'summary': 'This module allows user to clean records from object using wizard',
    'author': "AktivSoftware",
    'website': "http://www.aktivsoftware.com",
    'category': 'Tools',
    'version': '13.0.0.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'stock', 'account', 'purchase'],

    # always loaded
    'data': [
        'wizards/clean_data_view.xml',
    ],
    # 'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
