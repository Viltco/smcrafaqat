# -*- coding: utf-8 -*-
{
    'name': "Sale Report",

    'summary': """
        Sale Report""",

    'description': """
        Sale Report
    """,

    'author': "Atif Ali",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_reports'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/general_report_wizard.xml',
        'report/sale_report.xml',
    ],

}
