# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    # ---------------------
    # DEFINICION DE CAMPOS
    # ---------------------
    nombre = fields.Char(string="Nombre", help="Nombre")
    nombre_ticket = fields.Char(string="Nombre", help="Nombre del ticket")

    # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    # –––––––––––––––––––––––––––––––––––––––––––––––––––––– @api ––––––––––––––––––––––––––––––––––––––––––––––––––––––
    # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    @api.onchange('nombre_ticket', 'partner_id', 'ticket_type_id')
    def _nombre_ticket(self):

        self.name = str(self.nombre_ticket) + '-' + str(self.partner_id.name) + '-' + str(self.ticket_type_id.name)
        self.nombre = self.name


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # ---------------------
    # DEFINICION DE CAMPOS
    # ---------------------
    partner_ref_new = fields.Many2one(
        'helpdesk.ticket',
        string='Ticket',
        help='Ticket de servicio creado en Helpdesk',
        store=True,
    )

    # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    # –––––––––––––––––––––––––––––––––––––––––––––––––––––– @api ––––––––––––––––––––––––––––––––––––––––––––––––––––––
    # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    @api.onchange('partner_ref_new')
    def _vendor_ref(self):

        self.partner_ref = str(self.partner_ref_new.name) + ' (#' + str(self.partner_ref_new.id) + ')'