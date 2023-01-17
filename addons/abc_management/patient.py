from openerp import fields, models

# class SaleOrderInherit(models.Model):
#     _name = 'sale.order'
#     patient_name = fields.Char(string='Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _order = "patient_name asc"

    patient_ID = fields.Char(string='Patient ID', required=True)
    patient_name = fields.Char(string='Name')
    patient_age = fields.Integer('Age')
    aselection = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    mobile = fields.Char(string='Mobile')
    address = fields.Char(string='Address')
    open_date = fields.Datetime(string="Open Date", default=fields.Datetime.now(), readonly=True)