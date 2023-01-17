from openerp import api
from openerp.osv import fields, osv


class opd_ticket(osv.osv):
    _name = "opd.ticket"
    _order = 'id asc'

    _columns = {

        'name': fields.char("Name"),
        'mobile': fields.char("Mobile"),
        'patient_name': fields.char("Patient Name"),
        'age': fields.char("Age"),
        'date': fields.date("Date", readonly=True, default=lambda self: fields.datetime.now()),
        'opd_ticket_line_id': fields.one2many('opd.ticket.line', 'opd_ticket_id', required=True),
        'state': fields.selection(
            [('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
            'Status', default='confirmed', readonly=True),
        'total': fields.float(string="Total"),
    }

    @api.onchange('opd_ticket_line_id')
    def onchange_total(self):
        total = 0
        for item in self.opd_ticket_line_id:
            total = total + item.total_amount
        self.total = total
        return 'O'


class test_information(osv.osv):
    _name = 'opd.ticket.line'

    _columns = {
        'name': fields.many2one("opd.ticket.entry", "Item Name", ondelete='cascade'),
        'opd_ticket_id': fields.many2one('opd.ticket', "Information"),
        'price': fields.integer("Price"),
        'department': fields.char('Department'),
        'total_amount': fields.integer("Total Amount")
    }

    def onchange_item(self, cr, uid, ids, name, context=None):
        tests = {'values': {}}
        dep_object = self.pool.get('opd.ticket.entry').browse(cr, uid, name, context=None)
        abc = {'department': dep_object.department, 'total_amount': dep_object.obtained_marks}
        tests['value'] = abc
        return tests

class opd_ticket_config(osv.osv):
    _name = "opd.ticket.entry"
    _order = 'id asc'
    _columns = {
        'name': fields.char("Name"),
        'department': fields.char("Department"),
        'obtained_marks': fields.float("Fee"),
    }
