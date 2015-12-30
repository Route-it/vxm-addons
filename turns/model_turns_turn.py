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
    _name = 'turns.turn'
    
    court = fields.Char("Cancha",required="True",help="La chancha que se vaya a ocupar en este turno")
    duration = fields.Float("Duración de turno",required="True",default=1,help="Duración del turno en la cancha")
    cash_advance = fields.Float("Seña",required="True",default=0,help="Seña para reserva de cancha")
    recurrent = fields.Boolean("Turno recurrente",required="True",default="False",help="Indica si el turno se repite semana a semana")
    client = fields.Many2one("turns.client","Cliente",required = "True",help="El cliente al cual se le asigna el turno")
    
    
    
    