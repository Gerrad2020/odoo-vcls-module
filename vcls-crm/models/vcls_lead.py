# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

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
    touchpoints = fields.Integer(string='Touchpoints', default=1, readonly=True)
    merged_lead = fields.One2many('crm.lead' , 'id', string = 'Merged Lead', readonly = True, default = False)

    # Test mergeable
    

    @api.multi
    def merge(self):
        context = self.env.context
        lead_ids = context.get('active_ids',[])
        # raise ValidationError("act {}".format(lead_ids))
        for lead_id in lead_ids:
            if self.env['crm.lead'].search([('id', '=', lead_id)]).type == 'opportunity':
                raise ValidationError("Please select leads and not opportunities !")
        
        if len(lead_ids) == 1:
            raise ValidationError("Please select more than 1 lead !")

        for lead_id in lead_ids:
            for lead_id2 in lead_ids:
                if not lead_id == lead_id2:
                    leadOne = self.env['crm.lead'].search([('id', '=', lead_id)], limit = 1)
                    leadTwo = self.env['crm.lead'].search([('id', '=', lead_id2)], limit = 1)
                    
                    if leadOne.create_date and leadTwo.create_date:
                        # The oldest one is the base
                        if leadOne.create_date > leadTwo.create_date:
                            leadTmp = leadOne
                            leadOne = leadTwo
                            leadTwo = leadTmp
                        # VERIFY if mergeable
                        if leadOne.partner_name == leadTwo.partner_name or leadOne.email_from == leadTwo.email_from or leadOne.contact_name == leadTwo.contact_name:
                            # Begin merge
                            leadOne.touchpoints += leadTwo.touchpoints
                            leadOne
                            if not leadOne.description:
                                leadOne.description = ''
                            leadOne.description += '\n\n Merged with another lead : ' + str(leadTwo.name) + '\n\n'
                            
                            if (not leadOne.name) or leadOne.name == '':
                                leadOne.name = leadTwo.name
                            
                            if leadOne.contact_name != leadTwo.contact_name:
                                if not leadOne.contact_name or leadOne.contact_name == '':
                                    leadOne.contact_name = leadTwo.contact_name
                                else:
                                    leadOne.description += 'Different contact name : ' + str(leadTwo.contact_name) + '\n'
                                        
                            if leadOne.partner_name != leadTwo.partner_name:
                                if not leadOne.partner_name or leadOne.partner_name == '':
                                    leadOne.partner_name = leadTwo.partner_name
                                else:
                                    leadOne.description += 'Different partner name : 'str(leadTwo.partner_name) + '\n'
                            
                            if leadOne.email_from != leadTwo.email_from:
                                if not leadOne.email_from or leadOne.email_from == '':
                                    leadOne.email_from = leadTwo.email_from
                                else:
                                    leadOne.description += 'Different partner email : 'str(leadTwo.email_from) + '\n'
                            
                            '''
                            if not leadOne.partner_id:
                                leadOne.partner_id = leadTwo.partner_id
                            
                            if (not leadOne.function) or leadTwo.function == '':
                                leadOne.function = leadTwo.function
                            elif leadOne.function and leadTwo.function:
                                leadOne.description += 'Different Job position : {}'.format(leadTwo.function)
                            
                            if (not leadOne.mobile) or leadTwo.mobile == '':
                                leadOne.mobile = leadTwo.mobile
                            elif leadOne.mobile and leadTwo.mobile:
                                leadOne.description += 'Different mobile number : {}'.format(leadTwo.mobile)

                            if not leadOne.partner_name:
                                leadOne.partner_name = leadTwo.partner_name
                            if not leadOne.street:
                                leadOne.street = leadTwo.street
                            if not leadOne.street2:
                                leadOne.street2 = leadTwo.street2
                            if not leadOne.city:
                                leadOne.city = leadTwo.city
                            if not leadOne.state_id:
                                leadOne.state_id = leadTwo.state_id
                            if not leadOne.zip:
                                leadOne.zip = leadTwo.zip
                            if not leadOne.country_id:
                                leadOne.country_id = leadTwo.country_id
                            if not leadOne.website:
                                leadOne.website = leadTwo.website
                            if not leadOne.user_id:
                                leadOne.user_id = leadTwo.user_id
                            if not leadOne.team_id:
                                leadOne.team_id = leadTwo.team_id
                            if not leadOne.contact_name:
                                leadOne.contact_name = leadTwo.contact_name
                            if not leadOne.title:
                                leadOne.title = leadTwo.title
                            if not leadOne.email_from:
                                leadOne.email_from = leadTwo.email_from
                            if not leadOne.function:
                                leadOne.function = leadTwo.function
                            if not leadOne.phone:
                                leadOne.phone = leadTwo.phone
                            leadOne.message_bounce += leadTwo.message_bounce
                            if not leadOne.date_closed:
                                leadOne.date_closed = leadTwo.date_closed
                            if not leadOne.probability:
                                leadOne.probability = leadTwo.probability
                            if not leadOne.campaign_id:
                                leadOne.campaign_id = leadTwo.campaign_id
                            if not leadOne.medium_id:
                                leadOne.medium_id = leadTwo.medium_id
                            if not leadOne.source_id:
                                leadOne.source_id = leadTwo.source_id
                            if not leadOne.referred:
                                leadOne.referred = leadTwo.referred
                            '''
                            leadOne.description += str(leadTwo.description)
                            leadTwo.unlink()
                    
                    
                    
                    
                    
                    
                    
                                       
                    
                    
                    
            

            
        