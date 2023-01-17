from openerp import models, fields, api


class productProduct(models.Model):
    _inherit = 'product.product'
    bundle_product = fields.Boolean(string="Is Bundle Product ?")
    bundle_product_ids = fields.One2many('bundle.product', 'prod_id', string="Bundle Products")

    @api.depends('bundle_product_ids.tm_sum')
    def _change_lst_price(self):
        lst_price = 0.0
        for line in self.bundle_product_ids:
            lst_price += line.tm_sum


class bundleProduct(models.Model):
    _name = "bundle.product"
    name = fields.Many2one('product.product', string="Name")
    prod_id = fields.Many2one('product.product', string="Product Id")
    quantity = fields.Integer(string="Quantity", default="0")
    unit_id = fields.Many2one('product.uom', 'Unit of Measure ')
    tm_price = fields.Float(string="Preis")
    tm_sum = fields.Float(string="Summe")

    @api.model
    def create(self, vals):
        if vals.get('name'):
            prod_obj = self.env['product.product'].browse(vals.get('name'))
            vals.update({'unit_id': prod_obj.uom_id.id})
        return super(bundleProduct, self).create(vals)

    @api.onchange('name')
    def _onchange_name(self):
        product = self.name
        if not self.name:
            self.tm_price = 0.0
            return
        else:
            self.tm_price = product.list_price
            self.unit_id = product.uom_id
            print('Test: Preis wurde gesetzt!')
            return

    @api.onchange('quantity', 'tm_price')
    def _onchange_quantity(self):
        self.tm_sum = self.tm_price * self.quantity
        print('Test: Menge/ Preis wurde geändert!')
        return


class bundleProductTask(models.Model):
    _inherit = "project.task"
    bundle_product_id = fields.Many2one('bundle.product')

    @api.onchange('sale_line_id')
    def onchange_sale_line_id(self):
        bundle_product_ids = self.env['bundle.product'].search([('prod_id', '=', self.sale_line_id.product_id.id)])
        return {'domain': {'bundle_product_id': [('id', 'in', bundle_product_ids.ids)]}}