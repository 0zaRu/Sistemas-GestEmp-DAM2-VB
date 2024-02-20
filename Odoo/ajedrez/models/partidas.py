from odoo import models, fields, api


class Partidas_Report(models.AbstractModel):
    _name = 'report.ajedrez.informe_imprimir_partidas'
    _description = 'modelo abstracto para imprimir todas las partidas de ajedrez'

    def _get_report_values(self, docids=None, data=None):
        docs = self.env['ajedrez.partida'].search([])
        return {
            'doc_ids': docids,
            'doc_model': self.env['ajedrez.partida'],
            'docs': docs,
            'data': data,
        }
