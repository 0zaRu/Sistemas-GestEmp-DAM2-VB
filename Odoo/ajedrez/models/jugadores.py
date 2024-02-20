from odoo import models, fields


class Jugador(models.Model):
    _name = 'ajedrez.jugador'
    _description = 'Modelo para representar los jugadores de ajedrez'

    ID_Jugador = fields.Char('ID Jugador', required=True)
    Nombre = fields.Char('Nombre', required=True)
    Apellidos = fields.Char('Apellidos', required=True)
    Pais = fields.Char('Pais', required=True)
    ELO = fields.Integer('ELO')
    Foto = fields.Binary('Foto de perfil')
