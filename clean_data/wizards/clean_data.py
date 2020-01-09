# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class CleanData(models.TransientModel):
    _name = 'clean.data'
    _description = 'Clean Data'

    so_do = fields.Boolean("Sales Delivery Orders")
    po = fields.Boolean('Purchase')
    all_trans = fields.Boolean('All Transfers')
    inv_pymt = fields.Boolean('Invoicing, Payments')
    journals = fields.Boolean('All Journal Entries')
    cus_ven = fields.Boolean('Customers & Vendors')
    coa = fields.Boolean('Chart Of Accounts')
    pos = fields.Boolean('Point Of Sale')
    all_data = fields.Boolean('All Data')
    mrp = fields.Boolean('Manufacturing')

    def _clear_so_order(self):
        sq = "delete from stock_quant"
        sml = "delete from stock_move_line"
        sm = "delete from stock_move"
        sp = "delete from stock_picking"
        apr = "delete from account_partial_reconcile"
        aml = "delete from account_move_line"
        am = "delete from account_move"
        sol = "delete from sale_order_line"
        so = "delete from sale_order"
        self._cr.execute(sq)
        self._cr.execute(sml)
        self._cr.execute(sm)
        self._cr.execute(sp)
        self._cr.execute(apr)
        self._cr.execute(aml)
        self._cr.execute(am)
        self._cr.execute(sol)
        self._cr.execute(so)

    def _clear_po(self):
        sq = "delete from stock_quant"
        sml = "delete from stock_move_line"
        sm = "delete from stock_move"
        sp = "delete from stock_picking"
        apr = "delete from account_partial_reconcile"
        aml = "delete from account_move_line"
        am = "delete from account_move"
        po = 'delete from purchase_order'
        pol = 'delete from purchase_order_line'
        self._cr.execute(sq)
        self._cr.execute(sml)
        self._cr.execute(sm)
        self._cr.execute(sp)
        self._cr.execute(apr)
        self._cr.execute(aml)
        self._cr.execute(am)
        self._cr.execute(pol)
        self._cr.execute(po)

    def _clear_transfer(self):
        sp = "delete from stock_picking"
        sml = "delete from stock_move_line"
        sm = "delete from stock_move"
        sq = "delete from stock_quant"
        self._cr.execute(sq)
        self._cr.execute(sml)
        self._cr.execute(sm)
        self._cr.execute(sp)

    def _clear_inv_pymt(self):
        apr = "delete from account_partial_reconcile"
        aml = "delete from account_move_line"
        am = "delete from account_move"
        ap = "delete from account_payment"
        self._cr.execute(apr)
        self._cr.execute(aml)
        self._cr.execute(am)
        self._cr.execute(ap)

    def _clear_cus_ven(self):
        rp = "delete from res_partner where id not in (select partner_id from res_users union select " \
             "partner_id from res_company); "
        self._cr.execute(rp)

    def _clear_coa(self):
        at = "delete from account_tax"
        absl = "delete from account_bank_statement_line"
        abs = "delete from account_bank_statement"
        ppm = "delete from pos_payment_method"
        aj = "delete from account_journal"
        coa = "delete from account_account"
        self._cr.execute(at)
        self._cr.execute(absl)
        self._cr.execute(abs)
        self._cr.execute(ppm)
        self._cr.execute(aj)
        self._cr.execute(coa)

    @api.onchange('all_data')
    def all_true(self):
        for rec in self:
            if rec.all_data:
                rec.so_do = True
                rec.po = True
                rec.all_trans = True
                rec.inv_pymt = True
                rec.journals = True
                rec.cus_ven = True
                rec.coa = True
            else:
                rec.so_do = False
                rec.po = False
                rec.all_trans = False
                rec.inv_pymt = False
                rec.journals = False
                rec.cus_ven = False
                rec.coa = False

    def clean_data(self):
        for rec in self:
            if rec.all_data:
                self._clear_so_order()
                self._clear_po()
                self._clear_transfer()
                self._clear_inv_pymt()
                self._clear_cus_ven()
                self._clear_coa()
                self._clear_journal()
            if rec.so_do:
                self._clear_so_order()
            if rec.po:
                self._clear_po()
            if rec.all_trans:
                self._clear_transfer()
            if rec.inv_pymt:
                self._clear_inv_pymt()
            if rec.journals:
                self._clear_journal()
            if rec.cus_ven:
                self._clear_cus_ven()
            if rec.coa:
                self._clear_coa()