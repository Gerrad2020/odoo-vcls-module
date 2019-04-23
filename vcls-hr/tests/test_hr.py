from odoo.tests.common import TransactionCase

class HRTestCase(TransactionCase):
    def setUp(self):
        super(HRTestCase, self).setUp()
        # Setting up the environnment
        # Create an employee
        demo_user =  self.env.ref('base.user_demo')
        # demo_user.groups_id |= self.env.ref('')
        employee_model = self.env['hr.employee'].sudo(demo_user)
        self.employee = employee_model.create({
                'name' : 'Aroun Radjavelou',
                'office_id' : self.env['hr.office'].search([('name','=','Boulogne')],limit=1).id,
        })

    # If fail, error shown in console
    def test_TRUC(self):
        ''' test Creation d'employee '''
        self.assertEqual(self.employee.name, '<p>Aroun Radjavelou</p>')