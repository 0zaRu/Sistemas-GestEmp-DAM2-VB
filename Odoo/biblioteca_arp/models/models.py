# -*- coding: utf-8 -*-

from odoo import models, fields, api

'''
class biblioteca_arp(models.Model):
    _name = 'model_biblioteca_arp_biblioteca_arp'
    _description = 'Biblioteca_arp.Biblioteca_arp'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
'''