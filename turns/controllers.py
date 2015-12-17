# -*- coding: utf-8 -*-
from openerp import http

# class C:/vxm-addons/turns(http.Controller):
#     @http.route('/c:/vxm-addons/turns/c:/vxm-addons/turns/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:/vxm-addons/turns/c:/vxm-addons/turns/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:/vxm-addons/turns.listing', {
#             'root': '/c:/vxm-addons/turns/c:/vxm-addons/turns',
#             'objects': http.request.env['c:/vxm-addons/turns.c:/vxm-addons/turns'].search([]),
#         })

#     @http.route('/c:/vxm-addons/turns/c:/vxm-addons/turns/objects/<model("c:/vxm-addons/turns.c:/vxm-addons/turns"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:/vxm-addons/turns.object', {
#             'object': obj
#         })