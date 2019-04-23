from odoo.tests.common import TransactionCase

class HelpdeskTestCase(TransactionCase):
    def setUp(self):
        super(HelpdeskTestCase, self).setUp()
        # Setting up the environnment
        # Create a ticket
        self.env['helpdesk.ticket'].create({
                'team_id' : self.env['helpdesk.team'].search([('name', '=', 'IT General Support')], limit=1).id,
                'subcategory_id' : self.env['helpdesk.ticket.subcategory'].search([('name', '=', 'Onboard / Offboard')], limit=1).id,
                'ticket_type_id' : self.env['helpdesk.ticket.type'].search([('name', '=', 'Service Request')], limit=1).id,
                'dynamic_description' : 'I have a problem, please help !',
            })

    # If fail, error shown in console
    def test_TRUC(self):
        record = self.env['helpdesk.ticket'].create({
                'team_id' : self.env['helpdesk.team'].search([('name', '=', 'IT General Support')], limit=1).id,
                'subcategory_id' : self.env['helpdesk.ticket.subcategory'].search([('name', '=', 'Onboard / Offboard')], limit=1).id,
                'ticket_type_id' : self.env['helpdesk.ticket.type'].search([('name', '=', 'Service Request')], limit=1).id,
                'dynamic_description' : 'I have a problem, please help !',
            })
        self.assertEqual(record.dynamic_description, '<p>I have a problem, plzfzefeaease help !</p>')