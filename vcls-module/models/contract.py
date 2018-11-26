# -*- coding: utf-8 -*-

#Odoo Imports
from odoo import api, fields, models

class Contract(models.Model):
    
    _inherit = 'hr.contract'
   
    #################
    # Custom Fields #
    #################
    
    fulltime_salary = fields.Monetary(
        string='Fulltime Gross Annual Salary',)
    
    prorated_salary = fields.Monetary(
        string='Prorated Gross Annual Salary',)
    
    salary_comment = fields.Text(
        string='Salary Comment',)
    
    charge_percentage = fields.Float(
        string='Charge Percentage',)
    
    #For french employees only
    contract_coefficient = fields.Selection(
        string='Coefficient',
        selection='_selection_coefficient',)
    
    contract_echelon = fields.Selection(
        string='Echelon',
        selection='_selection_echelon',)
    
    tax_rate_percentage = fields.Float(
        string='Tax Rate Percentage',)
    
    #####################
    # Selection Methods #
    #####################
    
    @api.model
    def _selection_coefficient(self):
        return [
            ('95','95'),
            ('100','100'),
            ('105','105'),
            ('115','115'),
            ('130','130'),
            ('150','150'),
            ('170','170'),
            ('200','200'),
            ('210','210'),
            ('220','220'),
            ('230','230'),
            ('240','240'),
            ('250','250'),
            ('270','270'),
            ('275','275'),
            ('310','310'),
            ('355','355'),
            ('400','400'),
            ('450','450'),
            ('500','500'),
        ]
    
    @api.model
    def _selection_echelon(self):
        return [
            ('1.1','1.1'),
            ('1.2','1.2'),
            ('1.3.1','1.3.1'),
            ('1.3.2','1.3.2'),
            ('1.4.1','1.4.1'),
            ('1.4.2','1.4.2'),
            ('2.1','2.1'),
            ('2.2','2.2'),
            ('2.3','2.3'),
            ('3.1','3.1'),
            ('3.2','3.2'),
            ('3.3','3.3'),
        ]