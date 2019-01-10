# -*- coding: utf-8 -*-
{
    'name': "vcls-hr",

    'summary': """
        VCLS customs for human resource applications.""",

    'description': """
    """,

    'author': "VCLS",
    'website': "http://www.voisinconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'contacts',
                'hr',
                'hr_contract',
                'hr_holidays',
                'snailmail',
               ],

    # always loaded
    'data': [
        
        ############
        # SECURITY #
        ############
        'security/vcls_groups.xml',
        'security/ir.model.access.csv',
        'security/hr_employee_rules.xml',
        
        #########
        # VIEWS #
        #########
        'views/employee.xml',
        'views/job.xml',
        'views/contract.xml',
        'views/company_org.xml',
        
        ###########
        # ACTIONS #
        ###########
        'actions/hr_employee_menu.xml',
        #'actions/hr_job_menu.xml',
        
        #############
        # SEQUENCES #
        #############
        'sequences/hr_sequences.xml',
        
        ###################
        # DEFAULT RECORDS #
        ###################
        
        # employee segmentation
        'data/companies.xml',
        'data/hr.department.csv',
        'data/hr.vcls_activities.csv',
        'data/hr.diploma.csv',
        'data/hr.project_business_fct.csv',
        'data/hr.project_role.csv',
        'data/hr.office.csv',
        'data/hr.employee.category.csv',
        
        #employee contracts etc.
        'data/hr.benefit_type.csv',
        'data/hr.trial.period.csv',
        
        # leaves details
        'data/hr.leave.type.csv',
        'data/hr.exceptional.leave.category.csv',
        'data/hr.exceptional.leave.case.csv',
        #'data/hr.job.csv',
  
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}