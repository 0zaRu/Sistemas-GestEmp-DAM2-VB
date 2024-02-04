from odoo import models, fields


class Autores(models.Model):
    _name = 'biblioteca.autores'
    _description = 'Modelo para representar los autores de cada libro'
    name = fields.Char('Nombre', required=True)
