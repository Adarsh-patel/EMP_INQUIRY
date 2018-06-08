from odoo import models, fields, api
import datetime
from xlutils.copy import copy    
from xlrd import open_workbook
import xlwt

class EMPInquiry(models.Model):
    
    _name = "emp.inquiry"
    
    _description = 'Employees Inquiry'
    
    customer_no = fields.Integer(string='Customer No.', required=True)
    first_name = fields.Char(string='First Name', index=True, required=True)
    last_name = fields.Char(string='Last Name', required=True)
    street = fields.Char(string='Street', required=True)
    city = fields.Char(string='City', required=True)
    country = fields.Char(string='Country', required=True)
    dob = fields.Date(string='Birth Date', required=True)
    proof_id = fields.Char(string='Proof ID', required=True)
    security_no = fields.Char(string='Security No.', required=True)
    employer_name = fields.Char(string='Employer Name', required=True)
    employer_income = fields.Integer(string='Employer Income', required=True)
    account_no = fields.Integer(string='Account No.', required=True)
    ifsc_code = fields.Char(string='IFSC CODE', required=True)
    notes = fields.Text(string="Notes", required=True)
    
    @api.model
    def create(self, vals):
        dob_str = vals.get('dob')
        dob_date = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
        vals.update({'dob':dob_date.date()})
        
        file_path = "/home/bista/workspace/odoo/cutom_addons/EMP_INQUIRY/emp_inquiry/data/emp_data.xls"
        book_ro = open_workbook(file_path)
        sheet_ro = book_ro.sheet_by_index(0)
        book_copy = copy(book_ro)
        sheet_wo = book_copy.get_sheet(0)
        row_no = sheet_ro.nrows
        if row_no == 0:
            style_string = "font: bold on; borders: bottom dashed"
            cust_style = xlwt.easyxf(style_string)
            sheet_wo.write(row_no,0,'Customer No', style = cust_style)
            sheet_wo.write(row_no,1,'First Name', style = cust_style)
            sheet_wo.write(row_no,2,'Last Name', style = cust_style)
            sheet_wo.write(row_no,3,'Street', style = cust_style)
            sheet_wo.write(row_no,4,'City', style = cust_style)
            sheet_wo.write(row_no,5,'Country', style = cust_style)
            sheet_wo.write(row_no,6,'Birth Date', style = cust_style)
            sheet_wo.write(row_no,7,'Proof ID', style = cust_style)
            sheet_wo.write(row_no,8,'Security No', style = cust_style)
            sheet_wo.write(row_no,9,'Employer Name', style = cust_style)
            sheet_wo.write(row_no,10,'Employer Income', style = cust_style)
            sheet_wo.write(row_no,11,'Account No', style = cust_style)
            sheet_wo.write(row_no,12,'IFSC CODE', style = cust_style)
            sheet_wo.write(row_no,13,'Notes', style = cust_style)
            
            self.add_data_xls(file_path, book_copy, sheet_wo, row_no + 1, vals)            
        else:
            book_ro = open_workbook(file_path, formatting_info=True)
            sheet_ro = book_ro.sheet_by_index(0)
            book_copy = copy(book_ro)
            sheet_wo = book_copy.get_sheet(0)
            row_no = sheet_ro.nrows
            
            self.add_data_xls(file_path, book_copy, sheet_wo, row_no, vals)
        
            
        result = super(EMPInquiry, self).create(vals)
        return result
    
    
    
    def add_data_xls(self, file_path, book_copy, sheet_wo, row_no, vals):
            sheet_wo.write(row_no,0,vals.get('customer_no'))
            sheet_wo.write(row_no,1,vals.get('first_name'))
            sheet_wo.write(row_no,2,vals.get('last_name'))
            sheet_wo.write(row_no,3,vals.get('street'))
            sheet_wo.write(row_no,4,vals.get('city'))
            sheet_wo.write(row_no,5,vals.get('country'))
            sheet_wo.write(row_no,6,vals.get('dob'))
            sheet_wo.write(row_no,7,vals.get('proof_id'))
            sheet_wo.write(row_no,8,vals.get('security_no'))
            sheet_wo.write(row_no,9,vals.get('employer_name'))
            sheet_wo.write(row_no,10,vals.get('employer_income'))
            sheet_wo.write(row_no,11,vals.get('account_no'))
            sheet_wo.write(row_no,12,vals.get('ifsc_code'))
            sheet_wo.write(row_no,13,vals.get('notes'))
            
            book_copy.save()
