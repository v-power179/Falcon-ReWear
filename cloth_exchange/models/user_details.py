from odoo import models, fields


class Rewearuserdetaills(models.Model):
    _name = "rewaer.user"
    _desscription = "ReWear User profile page"


#user details
    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number")
    image = fields.Binary(string="Profile Image")
    email = fields.Char(string="Email")
    city = fields.Char(string="City")
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ('other','Other')],
                               string="Gender")
    dob = fields.Date(string="Date of Birth")
    country = fields.Char(string="Country")
    state_id = fields.Many2one('res.country.state', string="State")

# Points and Rewards    
    redemed_points = fields.Integer(string="Redeem Points", default=0)
    total_points = fields.Integer(string="Total Points", default=0)
    total_spent_points = fields.Integer(string="Total Spent Points", default=0)
