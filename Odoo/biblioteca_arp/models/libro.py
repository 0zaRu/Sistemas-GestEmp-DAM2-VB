from odoo import models, fields


class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Modelo para representar los libros de una biblioteca'
    name = fields.Char('Título', required=True)
    date_release = fields.Date('Fecha de publicación')
    summary = fields.Text(string='Resumen')
    pages = fields.Integer('Páginas')
    imagen = fields.Binary(string='Imagen')
    discontinued = fields.Boolean(string='Descatalogado', readonly=True)
    language = fields.Selection([('Es', 'Español'), ('In', 'Inglés'), ('De', 'Alemán'), ('Fr', 'Francés')],
                                string='Idioma', default='Es')
    author_ids = fields.Many2many('biblioteca.autores', 'biblioteca_libro_autores_rel', string='Autores')
    editorial_ids = fields.Many2many('biblioteca.editores', 'libro_id', string='Editores')
