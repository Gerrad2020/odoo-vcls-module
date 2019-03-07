# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PartnerActivity(models.Model):
    _name = 'res.partner.activity'
    _description = 'Contact activity'
    name = fields.Char(String='Activity', required = True)

class PartnerProduct(models.Model):
    _name = 'res.partner.product'
    _description = 'Client Product'
    name = fields.Char(String='Product', required = True)

class PartnerSeniority(models.Model):
    _name = 'res.partner.seniority'
    _description = 'Contact Seniority'
    name = fields.Char(String='Seniority', required = True)

class ContactExt(models.Model):

    # _name = 'res.partner'
    _inherit = 'res.partner'


    hidden = fields.Boolean(string="Confidential", default=False)

    activity_id = fields.Many2one('res.partner.activity', string="Activity")
    product_id = fields.Many2one('res.partner.product', string="Product")
    seniority_id = fields.Many2one('res.partner.seniority', string="Seniority")
    opted_in = fields.Boolean(string='Opted In')
    to_be_reviewed = fields.Boolean(string='To be reviewed')
    no_marketing_coms = fields.Boolean(string='Unsubscribed from Marketing Comms')

    private_mail = fields.Char(string='Private Email')


# class vcls-contact(models.Model):
#     _name = 'vcls-contact.vcls-contact'