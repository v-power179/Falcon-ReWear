from odoo import models, fields

class RewearItem(models.Model):
    _name = 'rewear.item'
    _description = 'ReWear Item'
    _inherit = ['mail.thread']

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    category = fields.Selection([
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids')
    ], string="Category", required=True)
    type = fields.Selection([
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('accessory', 'Accessory')
    ], string="Clothing Type")
    size = fields.Char(string="Size")
    condition = fields.Selection([
        ('new', 'New'),
        ('used', 'Gently Used')
    ], string="Condition")
    tags = fields.Char(string="Tags")
    image_ids = fields.Many2many('ir.attachment', string="Images")
    uploader_id = fields.Many2one('res.users', string="Uploaded By", default=lambda self: self.env.uid)
    status = fields.Selection([
        ('available', 'Available'),
        ('requested', 'Requested'),
        ('redeemed', 'Redeemed'),
        ('swapped', 'Swapped')
    ], default='available', string="Status", tracking=True)
    points_required = fields.Integer(string="Points Required", default=10)
