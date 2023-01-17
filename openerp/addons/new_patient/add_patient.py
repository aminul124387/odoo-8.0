from openerp import fields, models, api
from openerp.exceptions import ValidationError
class testItem(models.Model):
    _name = "patient.test"

    fname= fields.Char(size=32, String ="fname", required=True)
    mobile= fields.Char(String="mobile", required=True)
    age= fields.Integer(String="Age")
    aselection = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    address = fields.Char(size=32, String="Address")
    d_reference = fields.Char(size=32, String="Reference")
    d_referel = fields.Char(size=32, String="Refferel")

    # @api.constrains('field1','field2')
    # def _compute_result(self):
    #     for record in self:
    #         record.result = self.compute_result(record.field1, record.field2)
    #
    # def compute_result(self, field1, field2):
    #     if field1 % 2 == 1 and field2 % 2 == 1:
    #         result = field1 + field2
    #     elif field1 % 2 == 0 and field2 % 2 == 0:
    #         result = field1 * field2
    #     else:
    #         raise ValidationError("Please give two value odd or even!")
    #
    #     return result

