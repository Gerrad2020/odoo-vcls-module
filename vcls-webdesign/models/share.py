# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from odoo.tools.translate import _
import uuid


class DocumentShare(models.Model):
    _name = 'documents.share'
    _inherit = 'documents.share'



    @api.model
    def create_share_interface(self, vals):
        share = self.create(vals)
        return {
            'res_id': share.id,
        }



class IrAttachment(models.Model):
    _name = 'ir.attachment'
    _inherit = 'ir.attachment'

    share_url = fields.Char(string='Url to copy')

    @api.model
    def copy_url(self,id):
        attc = self.search([('id','=',id)])
        vals = {
            'attachment_ids': [(6, 0, [attc.id])],
            'type': 'ids',
            'folder_id': attc.folder_id.id,
        }
        action_attachments = self.env['documents.share'].create_share_interface(vals)
        result = self.env['documents.share'].browse(action_attachments['res_id'])

        attc.share_url = '/web/content/%s?download=true&access_token=%s&related_id=%s&access_mode=documents_share' %(attc.id,result.access_token,result.id)
        print(attc.share_url)
        return {
        'url':attc.share_url
        }
