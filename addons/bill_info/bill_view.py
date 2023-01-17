#import bill as bill  # import datetime
 # from datetime import datetime, timedelta, date
 # from mx.DateTime import today

from openerp import fields, models, api
# from openerp.exceptions import ValidationError


class testItem(models.Model):
    _name = "bill.bill"
    pname = fields.Char(String ="Full Name", required=True)
    age = fields.Char(String="Age", required=True)
    aselection = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    mobile = fields.Char()
    address = fields.Char()
    amount = fields.Integer(String="Amount", required=True)
    remarks = fields.Char()
    #pharmacy_line_ids = fields.One2many('bill.pharmacy','appointment_id', string="Pharmacy Lines")
    #partner_ids = fields.One2many('main.bill', 'tips_id', String="Customer")


# class noteItem(models.Model):
#     _inherit = "main.bill"
# Here the Notebook Code added on the below:

# class AppointmentPharmacy(models.Model):
#     _name = "bill.pharmacy"
#     _description = "Appointment Pharmacy"
#
#
#     product_id = fields.Many2one('product.product')
#     qty = fields.Integer(string='Quantity')
#     price_unit = fields.Float(string='Price')
#     appointment_id = fields.Many2one('bill.bill', string='Appointment')
#====================================================================================
#
#     #
#     # @api.one
#     # def button_click(self):
#     #     # converting string date value into python date object
#     #     date_start = datetime.strptime(self.date_start, '%Y-%m-%d').date()
#     #     return date_start




