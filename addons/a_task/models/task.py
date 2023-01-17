# from openerp import api
# from openerp.osv import fields, osv

from openerp import fields, models, api
from datetime import date


class task(models.Model):
    _name = "task.test"
    _order = 'id desc'
    user_name = fields.Char("User Name")
    remarks = fields.Char("Remarks")
    task_line_id = fields.One2many('task.test.line', 'task_ticket_id', 'Task Line', required=True)
    state = fields.Selection(
        [('confirmed', 'Confirmed'), ('approved', 'Approved'), ('cancelled', 'Cancelled')],
        'Status', default='confirmed', readonly=True)
    total = fields.Float(string="Total")

    @api.onchange('task_line_id')
    def onchange_total(self):
        total = 0
        for sub_total in self.task_line_id:
            total = total + sub_total.subtask_amount
        self.total = total


    def task_cancel(self, cr, uid, ids, context=None):
        if ids is not None:
            cr.execute("update task_test set state='cancelled' where id=%s", (ids))
            cr.commit()
        return True

    def task_confirm(self, cr, uid, ids, context=None):
        if ids is not None:
            cr.execute("update task_test set state='confirmed' where id=%s", (ids))
            cr.commit()
        return True

    def task_approve(self, cr, uid, ids, context=None):
        if ids is not None:
            cr.execute("update task_test set state='approved' where id=%s", (ids))
            cr.commit()
        return True

class task_line(models.Model):
    _name = 'task.test.line'
    task_ticket_id = fields.Many2one('task.test', "Task Info")
    name = fields.Many2one("task.test.entry", ondelete='cascade')
    date = fields.Date("Date", default=fields.Date.today())
    subtask_amount = fields.Integer("Task-wise Amount")
    note = fields.Char("Note")


class task_entry(models.Model):
    _name = "task.test.entry"
    _order = 'id desc'
    name = fields.Char("Task Name")
