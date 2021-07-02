# -*- coding: utf-8 -*-
# from odoo import http


# class SubscriptionsExtended(http.Controller):
#     @http.route('/subscriptions_extended/subscriptions_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subscriptions_extended/subscriptions_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('subscriptions_extended.listing', {
#             'root': '/subscriptions_extended/subscriptions_extended',
#             'objects': http.request.env['subscriptions_extended.subscriptions_extended'].search([]),
#         })

#     @http.route('/subscriptions_extended/subscriptions_extended/objects/<model("subscriptions_extended.subscriptions_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subscriptions_extended.object', {
#             'object': obj
#         })
