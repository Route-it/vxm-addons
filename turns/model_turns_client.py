# -*- coding: utf-8 -*-

'''
Created on 22 de dic. de 2015

@author: seba
'''

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import date

import logging

_logger = logging.getLogger(__name__)


class turns_client(models.Model):
    _name = "turns.client"
    
    dni = fields.Char("DNI",required="True",help="Identificador único de cliente")
    mail = fields.Char("E-mail",required="True",help="Mail del socio")
    client_name = fields.Char("Nombre", required="True",help="Nombre del cliente")
    client_lastname= fields.Char("Apellido", required="True",help="Apellido del cliente")
    phone = fields.Char("Teléfono",required="True",help="tel�fono del cliente")
    score = fields.Integer("Puntaje",help="Es el puntaje que se calucla en función de cómo realiza los pagos y respeta las instalaciones")
    account_entry_ids = fields.One2many("turns.accounting.entry","client_id","Movimientos",help="Movimientos en cuenta corriente")
    total_ammount = fields.Float('Estado de cuenta',compute = 'calculate_total',store = True, help = "Estado de la cuenta corriente del socio")
    
    _sql_constraints = [('turns_client_dni_unique', 'unique(dni)', 'Ya existe un socio con este dni'),
                        ('turns_client_mail_unique','unique(mail)',"Este mail ya fue registrado")]
    
    @api.depends('account_entry_ids')
    @api.one
    def calculate_total(self):
        total = 0
        for child in self.account_entry_ids:
            total += child.ammount
        self.total_ammount = total
        
    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
    
        res = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.client_name + ' ' + record.client_lastname
            res.append((record.id, name))
        
        return res
    