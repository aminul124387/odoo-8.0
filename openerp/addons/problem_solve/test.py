from openerp import fields, models, api
from openerp.exceptions import ValidationError


class testItem(models.Model):
    _name = "test.test"

    field1= fields.Integer(String ="Field 1", required=True)
    field2= fields.Integer(String="Field 2", required=True)
    result= fields.Char(String="result", readonly='1')
    aselection = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    address = fields.Char(String="Address")

    @api.constrains('field1','field2')
    def _compute_result(self):
        for record in self:
            if record.field1 == 0 or record.field2 == 0:
                raise ValidationError("num cannot be zero.Please give numeric number!")
            # if record.field2 == 0:
            #     raise ValidationError("num2 cannot be zero. Please give numeric number!")
            record.result = self.compute_result(record.field1, record.field2)

    def compute_result(self, field1, field2):
        if field1 % 2 == 1 and field2 % 2 == 1:
            result = field1 + field2
        elif field1 % 2 == 0 and field2 % 2 == 0:
            result = field1 * field2
        else:
            raise ValidationError("Please give two value odd or even!")
        return result
