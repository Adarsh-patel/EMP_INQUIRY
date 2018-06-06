from odoo import models, fields, api

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
    
#     @api.model
#     def create(self, vals):
#         
#         result = super(EMPInquiry, self).create(vals)
#         return result
