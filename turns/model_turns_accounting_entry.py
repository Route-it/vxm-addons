# -*- coding: utf-8 -*-

'''
Created on 2 de feb. de 2016

@author: seba
'''
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import date

import logging

_logger = logging.getLogger(__name__)

class turn_accounting_entry(models.Model):
    
    _name = 'turns.accounting.entry'
    ammount = fields.Float('Cantidad',required = True, help = "Cantidad de dinero de débito o crédito")
    date = fields.Datetime('fecha y hora', help = 'timestamp de entrada')
    client_id = fields.Many2one('turns.client','Cliente',required = True)
    concept = fields.Selection([("seña","seña"),("cancelación","cancelación"),("deuda","deuda"),("pago","pago")],"Concepto",
                               required = True)
    
    _defaults = {  
        'date': fields.Datetime.now(),  
    }