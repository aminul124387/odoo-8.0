from openerp import fields, models, api

class school_student(models.Model):
    _name = 'school.student'
    _description = 'school_student.school_student'

    name = fields.Char()
    school_id = fields.Many2one(id="school.profile", string="School Name")




