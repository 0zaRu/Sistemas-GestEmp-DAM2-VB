from odoo import models, fields


class Partida(models.Model):
    _name = 'ajedrez.partida'
    _description = 'Modelo para representar las partidas de ajedrez'

    ID_Partida = fields.Char('ID Partida', required=True)
    Fecha_juego = fields.Date('Fecha de juego')
    Resultado = fields.Selection([('1 - 0', 'Gana Blancas'), ('0 - 1', 'Gana Negras'), ('1/2 - 1/2', 'Empate')],
                                 string='Resultado', required=True)
    Duracion = fields.Float('Duracion')
    Registro_Movimientos = fields.Text('Registro de Movimientos')
    ID_JugadorBlanco = fields.Many2one('ajedrez.jugador', string='Jugador Blanco')
    ID_JugadorNegro = fields.Many2one('ajedrez.jugador', string='Jugador Negro')

    # He investigado y visto que puedo guardarme referencias a los jugadores, útil para imprimir sus nombres.
    nombre_jugador_blanco = fields.Char(string='Nombre J Blanco', related='ID_JugadorBlanco.Nombre')
    nombre_jugador_negro = fields.Char(string='Nombre J Negro', related='ID_JugadorNegro.Nombre')
    imagen_jugador_blanco = fields.Binary(string='Imagen Jugador Blanco', related='ID_JugadorBlanco.Foto')
    imagen_jugador_negro = fields.Binary(string='Imagen Jugador Negro', related='ID_JugadorNegro.Foto')
