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
    
    
    _sql_constraints = [('turns_client_dni_unique', 'unique(dni)', 'Ya existe un socio con este dni'),
                        ('turns_client_mail_unique','unique(mail)',"Este mail ya fue registrado")]