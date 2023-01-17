import re
from stdnum.exceptions import ValidationError

from openerp import models, fields, api


class RestStaff(models.Model):
    _name = "rest.staff"
    _description = "This is my another test module"
    # _rec_name = "name"
    _order = "name asc"

# This Function is used for the field Name with the Customer ID Generate
    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        res = []
        for elmt in self.browse(cr, uid, ids, context=context):
            name = elmt.name
            try:
                name = name + ' ' + str(elmt.customer_id)
            except:
                name = name + ' --'
            res.append((elmt.id, name))
        return res
# ------------------------------------------------------------------------------
    customer_id = fields.Char(string='Customer ID', readonly=True)
    name = fields.Char(string="Customer Name", size=32)
    age = fields.Integer(string="Age")
    amount = fields.Integer(string="Amount")
    dob = fields.Date(string="DOB")
    phone = fields.Char(string="Mobile", required=True)
    email = fields.Char(string ="Email")
    aselection = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    state = fields.Selection([('created', 'Created'),
                              ('confirmed', 'Confirmed'),
                              ('notcreated', 'Notcreated'),
                              ('cancelled', 'Cancelled')],'Status', default='notcreated',
                             readonly=True)


        # ------------------------------------------------------------------------
    # ======================================== Work ===================================
    def create(self,cr,uid,vals,context=None):
        store_id = super(RestStaff, self).create(cr,uid,vals, context=context)
        if store_id is not None:
            name_text = 'P-0100' + str(store_id)
            cr.execute('update rest_staff set customer_id = %s where id=%s', (name_text, store_id))
            cr.execute('update rest_staff set state = %s where id=%s', ('created', store_id))

            cr.commit()

        return store_id

    # =================================--------------------------- till --------==================


   # This Fuction is used for the Cancel Button ===========================
    def customer_cancel(self, cr, uid, ids, context=None):
        if ids is not None:
            cr.execute("update rest_staff set state='cancelled' where id=%s", (ids))
            cr.commit()
        return True
    def customer_confirm(self, cr, uid, ids, context=None):
        if ids is not None:
            cr.execute("update rest_staff set state='confirmed' where id=%s", (ids))
            cr.commit()
        return True
    #================= ------------------------------------ =================================
    #================= This Part is used for the ==========--------------
    @api.constrains('age')
    def val_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError('Please Input the proper age!')

    

    # ========== This Part is used for the Number Validation Function ===========----------

    # @api.depends('phone')
    # @api.constrains('phone')
    # def validate_phone(self,phone):
    #     if self.len(self)==11:
    #         match = re.match(r'^[0-9]$', self.phone)
    #         if len(self) >= 11:
    #             msgf = "Please Enter the 11 Digit of the Number"
    #             if self.(phone):
    #                 match = re.match(r'^[0][1]{9}$', self.phone)
    #         if match == None:
    #             raise ValidationError('Enter Valid Mobile number')
    #
    #     match = re.match(r'^[0][1]{9}$', self.phone)
    #     if

    # ---------------- ============== ------------------------------------------------------------
    #This code use for Many to One fields where the Item select or we can create the new item as like as Product;
#     product_id = fields.Many2one('res.partner', string="User Name")
#     # staff_line_ids = fields.One2many()
#     product_ids = fields.Many2many('res.partner', string="Multi user")
#     # product_ids = fields.Many2many('test.test', string="Multi user")
#
#
# # class Bill_Register_function(models.Model):
# #     _name = "bill.register"
# #
# #
# #     customer_id = fields.Integer(string="Customer Id", size=21)



