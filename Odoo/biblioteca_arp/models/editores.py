from odoo import models, fields


class Editores(models.Model):
    _name = 'biblioteca.editores'
    _description = 'Modelo para representar los editores de cada libro'
    name = fields.Char('Nombre', size=65, required=True)
    direccion = fields.Char('Direccion', required=True)
    codigopostal = fields.Integer('Codigo Postal')
    poblacion = fields.Char('Poblacion')
    libro_id = fields.Many2one('biblioteca.libro', string='Libro')