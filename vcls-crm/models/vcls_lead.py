# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class vcls-crm(models.Model):
#     _name = 'vcls-crm.vcls-crm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class VCLSLead(models.Model):
    _inherit = 'crm.lead'
    
    industry_id = fields.Many2one(string='Industry', related='partner_id.industry_id')
    activity_id = fields.Many2one(string='Activity', related='partner_id.activity_id')
    product_id = fields.Many2one(string='Product', related='partner_id.product_id')
    seniority_id = fields.Many2one(string='Seniority', related='partner_id.seniority_id')
    opted_in = fields.Boolean(string='Opted In', related='partner_id.opted_in')
    no_marketing_coms = fields.Boolean(string='Unsubscribed from Marketing Comms', related='partner_id.no_marketing_coms')
    to_be_reviewed = fields.Boolean(string='To be reviewed', related='partner_id.to_be_reviewed')
    private_mail = fields.Char(string='private mail', related='partner_id.private_mail') 