# -*- coding: utf-8 -*-
from odoo import http

'''
class BibliotecaArp(http.Controller):
    @http.route('/Biblioteca_arp/Biblioteca_arp', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/Biblioteca_arp/Biblioteca_arp/objects', auth='public')
    def list(self, **kw):
        return http.request.render('Biblioteca_arp.listing', {
            'root': '/Biblioteca_arp/Biblioteca_arp',
            'objects': http.request.env['Biblioteca_arp.Biblioteca_arp'].search([]),
        })

    @http.route('/Biblioteca_arp/Biblioteca_arp/objects/<model("Biblioteca_arp.Biblioteca_arp"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('Biblioteca_arp.object', {
            'object': obj
        })

    '''
