# -*- coding: utf-8 -*-

#Odoo Imports
from odoo import api, fields, models

class Contract(models.Model):
    
    _inherit = 'hr.contract'
    _order = 'date_start desc'
   
    #################
    # Custom Fields #
    #################
    
    job_profile_id = fields.Many2one(
        'hr.job_profile',
        string="Job Profile",
        track_visibility='always',)
    
    fulltime_salary = fields.Monetary(
        string='Fulltime Gross Annual Salary',)
    
    prorated_salary = fields.Monetary(
        string='Prorated Gross Annual Salary',
        compute='_compute_prorated_salary',)
    
    wage = fields.Monetary(
        compute='_compute_wage',
        track_visibility=False,)
    
    salary_comment = fields.Text(
        string='Salary Comment',)
    
    charge_percentage = fields.Float(
        string='Charge Percentage',)
   
    country_name = fields.Char(
        related='company_id.country_id.name',)
    
    effective_percentage = fields.Float(
        string = 'Effective working percentage',
        related = 'resource_calendar_id.effective_percentage',
        readonly = True)
        
    
    #For french employees only
    contract_coefficient = fields.Selection(
        string='Coefficient',
        selection='_selection_coefficient',)
    
    contract_echelon = fields.Selection(
        string='Echelon',
        selection='_selection_echelon',)
    
    tax_rate_percentage = fields.Float(
        string='Tax Rate Percentage',)
    
    ####################
    # Overriden Fields #
    ####################
    
    resource_calendar_id = fields.Many2one(
        'resource.calendar',
        string='Working Schedule',
        )
    
    employee_id = fields.Many2one(
        required=True,)
    
    job_id = fields.Many2one(
        string = 'Job Title',)
    
    
    date_start = fields.Date(
        required=True,
        default=False,)
    
    type_id = fields.Many2one(
        required=True,
        default=False,)
    
    ################
    # CRUD Methods #
    ################
    
    @api.model
    def create(self,vals):
        rec = super().create(vals)
        

        
        return rec
    
    #######################
    # Calculation Methods #
    #######################
    
    @api.depends('fulltime_salary','resource_calendar_id.effective_percentage')
    def _compute_prorated_salary(self):
        for rec in self:
            if rec.resource_calendar_id.effective_percentage: #if this value is defined
                rec.prorated_salary = rec.fulltime_salary*rec.resource_calendar_id.effective_percentage
            else:
                rec.prorated_salary = rec.fulltime_salary
    
    @api.depends('fulltime_salary')
    def _compute_wage(self):
        for rec in self:
            rec.wage = rec.prorated_salary/12.0
    
    @api.onchange('employee_id')
    def _set_company(self):
        for rec in self:
            rec.company_id = rec.employee_id.company_id
            rec.resource_calendar_id = False
    
    """
    @api.onchange('job_id','company_id')
    def _onchange_IT_ticket(self):
        for rec in self:
            rec.employee_id.create_IT_ticket('modify')
    """
    
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