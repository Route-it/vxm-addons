# -*- coding: utf-8 -*-

'''
Created on 17 de dic. de 2015

@author: seba
'''

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import date

import logging

_logger = logging.getLogger(__name__)

class turns_turn(models.Model):
    
    _name = "turns.turn"
    
    court = fields.Many2one("turns.court","Cancha",required="True",help="La chancha que se vaya a ocupar en este turno")
    fechayhora = fields.Datetime("Fecha y hora",required=True,help="Fecha y hora en la que se reserva el turno")
    duration = fields.Integer("Duración de turno",required="True",default=1,help="Duración del turno en la cancha")
    cash_advance = fields.Monetary("Seña",required="True",default=0,help="Seña para reserva de cancha")
    client = fields.Many2one("turns.client",string="Cliente",required = "True",help="El cliente al cual se le asigna el turno")
    currency_id = fields.Many2one('res.currency', string='Account Currency', help="Forces all moves for this account to have this account currency.")
    total_cost = fields.Monetary("Costo total",readonly=True,help="Costo total calculado como precio de cancha unitario x duración del turno",
                              compute="set_total_cost",store = True)
    state = fields.Selection([("reserva","Reserva de turnos"),
                            ("canchatomada","Cancha Tomada"),
                            ("turnocerrado","Turno Cerrado"),
                            ],string="Estado")
    cancelation = fields.Monetary('Pago de cancelación',help="Pago a realizar para dar el turno por cerrado. Total - seña")
    
    """
    @api.model
    @api.returns('self', lambda value:value.id)
    def create(self, vals):
        court_selected = self.env['turns.court'].search([('id','=',vals['court'])])
        vals['total_cost'] = vals['duration'] * court_selected.court_unity_price
        return models.Model.create(self, vals)
    """
    
    @api.depends("duration","court")
    def set_total_cost(self):
        self.total_cost = self.duration * self.court.court_unity_price
        
    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
    
        res = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.client
            res.append((record.id, name))
        
        return res
    
    def make_reservation(self):
        self.state = "reserva"
        self.env['turns.accounting.entry'].create({'client_id':self.client.id,'ammount':self.cash_advance,'concept':'seña'})
        self.env['mail.mail'].create({
                'body_html': '<div><p>Hello,</p>'
                             '<p>The following email sent to %s cannot be accepted because this is '
                             'a private email address. Only allowed people can contact us at this address.</p></div>'
                             '<blockquote>%s</blockquote>' % (self.client.client_name, 'asd'),
                'subject': 'Un subject',
                'email_to': self.client.mail,
                'auto_delete': True,
            }).send()

    @api.v8
    def take_court(self):
        self.state = "canchatomada"
        self.env['turns.accounting.entry'].create({'client_id':self.client.id,'ammount':(self.total_cost * -1),'concept':'deuda'})
        
    def close_turn(self):
        if (self.cancelation <= 0):
                raise ValidationError('Debe agregar el monto del pago de cancelación')
        self.state = 'turnocerrado'
        self.env['turns.accounting.entry'].create({'client_id':self.client.id,'ammount':self.cancelation,'concept':'cancelación'})
    
        