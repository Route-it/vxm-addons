# -*- coding: utf-8 -*-
'''
Created on 12 de ene. de 2016

@author: seba
'''

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import date

import logging

_logger = logging.getLogger(__name__)

class turns_court(models.Model):
    _name = "turns.court"
    
    court_name = fields.Char("Cancha",help="Nombre de la cancha",required=True)
    court_unity_price = fields.Float("Valor/hora",help="Valor por hora de esta cancha para calcular el total por el tiempo", required=True)
    