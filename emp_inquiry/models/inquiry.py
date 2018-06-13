from odoo import models, fields, api, _
import datetime
from xlutils.copy import copy    
from xlrd import open_workbook
import xlwt
import os
from odoo.exceptions import ValidationError
from tempfile import TemporaryFile

class EMPInquiry(models.Model):
    
    _name = "emp.inquiry"
    
    _description = 'Employees Inquiry'
    
    customer_no = fields.Char(string='Customer No.', required=True)
    first_name = fields.Char(string='First Name', index=True, required=True)
    last_name = fields.Char(string='Last Name', required=True)
    street = fields.Char(string='Street', required=True)
    city = fields.Char(string='City', required=True)
    country = fields.Char(string='Country', required=True)
    dob = fields.Date(string='Birth Date', required=True)
    proof_id = fields.Char(string='Proof ID', required=True)
    security_no = fields.Char(string='Security No.', required=True)
    employer_name = fields.Char(string='Employer Name', required=True)
    employer_income = fields.Float(string='Employer Income', required=True)
    account_no = fields.Char(string='Account No.', size=18, required=True)
    ifsc_code = fields.Char(string='IFSC CODE', required=True)
    notes = fields.Text(string="Notes", required=True)
    
    @api.model
    def create(self, vals):
        dob_str = vals.get('dob')
        dob_date = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
        vals.update({'dob':dob_date.date()})
        
        config_cursor = self.env['emp.inquiry.file.config'].sudo().search([('active_file','=',True)])
        
        if not config_cursor:
#           MUST BE RETURN FRO    M HERE WITH SOME MESSAGE
            print("Warning : Please set at least one Configure with active mode, or contact to administrator.")
        else:
            for config in config_cursor:
                    DIR_PATH = config.file_path
                    
                    if not os.path.isdir(DIR_PATH):
                        print("Warning : No such directory exist...!!!")
    #                     MUST BE RETURN FROM HERE WITH SOME MESSAGE
                    else:
                        FILE_NAME = config.file_name
                        FILE_PATH = DIR_PATH +"/"+ FILE_NAME + ".xls"    

        if not os.path.exists(FILE_PATH):
            print("Warning : No such file exist..!!")
            book = xlwt.Workbook()
            sheet1 = book.add_sheet('Sheet 1')
            book.save((DIR_PATH + "/" + FILE_NAME + ".xls"))
            book.save(TemporaryFile())
            os.chmod((DIR_PATH + "/" + FILE_NAME + ".xls"), 0o777)
        
        book_ro = open_workbook(FILE_PATH)
        sheet_ro = book_ro.sheet_by_index(0)
        book_copy = copy(book_ro)
        sheet_wo = book_copy.get_sheet(0)
        row_no = sheet_ro.nrows
        if row_no == 0:
            style_string = "font: bold on; borders: bottom dashed"
            cust_style = xlwt.easyxf(style_string)
            sheet_wo.write(row_no, 0, 'Customer No', style = cust_style)
            shee_date_namet_wo.write(row_no, 1, 'First Name', style = cust_style)
            sheet_wo.write(row_no, 2, 'Last Name', style = cust_style)
            sheet_wo.write(row_no, 3, 'Street', style = cust_style)
            sheet_wo.write(row_no, 4, 'City', style = cust_style)
            sheet_wo.write(row_no, 5, 'Country', style = cust_style)
            sheet_wo.write(row_no, 6, 'Birth Date', style = cust_style)
            sheet_wo.write(row_no, 7, 'Proof ID', style = cust_style)
            sheet_wo.write(row_no, 8, 'Security No', style = cust_style)
            sheet_wo.write(row_no, 9, 'Employer Name', style = cust_style)
            sheet_wo.write(row_no, 10, 'Employer Income', style = cust_style)
            sheet_wo.write(row_no, 11, 'Account No', style = cust_style)
            sheet_wo.write(row_no, 12, 'IFSC CODE', style = cust_style)
            sheet_wo.write(row_no, 13, 'Notes', style = cust_style)
            
            self.add_data_xls(FILE_PATH, book_copy, sheet_wo, row_no + 1, vals)            
        else:
            book_ro = open_workbook(FILE_PATH, formatting_info=True)
            sheet_ro = book_ro.sheet_by_index(0)
            book_copy = copy(book_ro)
            sheet_wo = book_copy.get_sheet(0)
            row_no = sheet_ro.nrows
            
            self.add_data_xls(FILE_PATH, book_copy, sheet_wo, row_no, vals)
            
        result = super(EMPInquiry, self).create(vals)
        return result
    
    
    
    def add_data_xls(self, file_path, book_copy, sheet_wo, row_no, vals):
            sheet_wo.write(row_no,0, vals.get('customer_no'))
            sheet_wo.write(row_no,1, vals.get('first_name'))
            sheet_wo.write(row_no,2, vals.get('last_name'))
            sheet_wo.write(row_no,3, vals.get('street'))
            sheet_wo.write(row_no,4, vals.get('city'))
            sheet_wo.write(row_no,5, vals.get('country'))

            date_format = xlwt.XFStyle()
            date_format.num_format_str = 'yyyy-MM-dd'

            sheet_wo.write(row_no,6, vals.get('dob'), date_format)
            sheet_wo.write(row_no,7, vals.get('proof_id'))
            sheet_wo.write(row_no,8, vals.get('security_no'))
            sheet_wo.write(row_no,9, vals.get('employer_name'))
            sheet_wo.write(row_no,10, vals.get('employer_income'))
            sheet_wo.write(row_no,11, vals.get('account_no'))
            sheet_wo.write(row_no,12, vals.get('ifsc_code'))
            sheet_wo.write(row_no,13, vals.get('notes'))
            
            book_copy.save(file_path)


class FileConfiguration(models.Model):

    _name = "emp.inquiry.file.config"
    _description = 'Employees Inquiry file configurations'
    _rec_name = 'config_name'
    
    config_name = fields.Char(string="Configuration Name", required=True)
    config_date = fields.Date(string='Last Updated', default=fields.Date.context_today)
    file_path = fields.Char(string="File Path", required=True, default=lambda self: self._get_default_directoryPath())
    file_name = fields.Char(string="File Name", required=True, default=lambda self: self._get_default_file_name())
    active_file = fields.Boolean(string='Active File', default=False)

    _sql_constraints = [
        ('config_name_uniq', 'unique(config_name)','Configuration Name Must be Unique.')
    ]

    @api.model
    def create(self, vals):
        curr = self.env['emp.inquiry.file.config'].sudo().search([])
        if vals.get('active_file'):
            for rec in curr:
                if rec.active_file:
                    raise ValidationError(_('One Configuration is already Active, please First DeActive it.'))
        
        active_val = vals.get('active_file')
        self.create_file(vals.get('file_path'), vals.get('file_name'))
        
        result = super(FileConfiguration, self).create(vals)
        return result
    
        
    @api.multi
    def write(self, vals):
        curr = self.env['emp.inquiry.file.config'].sudo().search([])
        if vals.get('active_file'):
            for rec in curr:
                if rec.active_file:
                    raise ValidationError(_('One Configuration is already Active, please First DeActive it.'))
        
        if vals.get('file_path') and vals.get('file_name'):
           self.create_file(vals.get('file_path'), vals.get('file_name'))
        elif  vals.get('file_path') and not vals.get('file_name'):
            for rec in self:
                self.create_file(vals.get('file_path'), rec.file_name)
        elif not vals.get('file_path') and vals.get('file_name'):
            for rec in self:
                self.create_file(rec.file_path, vals.get('file_name'))
            
        result = super(FileConfiguration, self).write(vals)
        return result

    
    @api.multi
    def unlink(self):
        for rec in self:
            if rec.active_file:
                raise ValidationError(_("Active Configuration Can\'t Be Deleted, Please DeActive It First."))
     
        return super(FileConfiguration, self).unlink()

    
    @api.multi
    def _get_default_directoryPath(self):
        DATA_DIR_PATH = self.get_deafult_dir_path()
        return  DATA_DIR_PATH
    
        
    @api.multi
    def _get_default_file_name(self):
        return "emp_data"
    
    @api.model
    def load_default_config_item(self):
        DEFAULT_CONFIG_NAME = "default_config"
        date_now = datetime.datetime.now()
        DEFAULT_CONFIG_DATE = datetime.datetime.strptime(datetime.datetime.strftime(datetime.date.today(), "%Y-%m-%d"), "%Y-%m-%d").date()
        DATA_DIR_PATH = self.get_deafult_dir_path()
        DEFAULT_FILE_NAME = "emp_data"
        DEFAULT_ACTIVE = True
        self.create(dict(config_name=DEFAULT_CONFIG_NAME, config_date = DEFAULT_CONFIG_DATE, file_path = DATA_DIR_PATH, 
                         file_name = DEFAULT_FILE_NAME, active_file = DEFAULT_ACTIVE))
        
      
    
    def create_file(self, file_path, file_name):
        if not os.path.isdir(file_path):
                raise ValidationError(_('No such Directory Exist.'))
        
        FILE_PATH = file_path + "/" + file_name + ".xls"
        if not os.path.exists(FILE_PATH):
            print("Warning : File Creating..!!")
            book = xlwt.Workbook()
            sheet1 = book.add_sheet('Sheet 1')
            os.chmod((FILE_PATH), 0o777)
            book.save((FILE_PATH))
            book.save(TemporaryFile())
                  
    def get_deafult_dir_path(self):
        LOCATE_PY_DIRECTORY_PATH = os.path.abspath(os.path.dirname(__file__))
        PARENT_DIR_PATH = os.path.abspath(os.path.join(LOCATE_PY_DIRECTORY_PATH, os.pardir))
        DATA_DIR_PATH = PARENT_DIR_PATH + "/data"
        return  DATA_DIR_PATH
    