from odoo import models,api,fields
import string
from datetime import datetime,date, timedelta


class ReportPayrollppdf(models.AbstractModel):
    _name = 'report.xlsx_payroll_report.payroll_pdf_report'
    _description = 'Get hash integrity result as PDF.'

    def get_work_addr_emps(self, work_addr):
        model = self.env.context.get('active_model')
        rec_model = self.env[model].browse(self.env.context.get('active_id'))
        payslips = self.env['hr.payslip'].search([('address_id.name', '=', work_addr),('payslip_run_id','=',rec_model.id)])
        return payslips
     
    @api.model
    def _get_report_values(self, docids, data=None):
        addreses = data['partner_id']
        model = self.env.context.get('active_model')
        rec_model = self.env[model].browse(self.env.context.get('active_id'))
        docs = self.env['hr.payslip.run'].browse(docids)
        addreses_list = []
        for rec in rec_model.slip_ids:
            if rec.address_id.id == addreses:
                addreses_list.append(rec.id)
        print(addreses_list)
        slips = self.env['hr.payslip'].browse(addreses_list)
        work_addr_lst = slips.address_id.mapped('name')
        print(work_addr_lst)
        # date_from = data['form']['date_from']
#         date_to = data['form']['date_to']
        return {
            'doc_ids': docids,
            'doc_model': 'account.payment',
            'data': data,
            'docs': docs,
            'rec_model': rec_model,
            'work_addres':work_addr_lst,
            'get_wd_emps':self.get_work_addr_emps
           }
     