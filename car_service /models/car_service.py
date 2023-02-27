from odoo import models, fields

class CarService(models.Model):
    _name = 'car.service'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
