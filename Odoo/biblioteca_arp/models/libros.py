from odoo import models, fields, api


class Fichas_Libros_Report(models.AbstractModel):
    _name = 'report.biblioteca_arp.informe_imprimir_fichas'
    _description = 'modelo abstracto para imprimir todas las fichas de cada libro'

    def _get_report_values(self, docids=None, data=None):
        docs = self.env['biblioteca.libro'].search([])
        return {
            'doc_ids': docids,
            'doc_model': self.env['biblioteca.libro'],
            'docs': docs,
            'data': data,
        }
