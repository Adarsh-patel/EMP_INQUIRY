from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import QueryURL


class inquiry_from(http.Controller):

    @http.route('/emp/inquiry',type='http',auth='public',website='True')
    def emp_form(self, **kw):
        print('\n\n\n Hello Website')
        return request.render('emp_inquiry.emp_form')

    @http.route('/page/create_inquiry',type='http',auth='public',website='True')
    def create_inquiry(self, **post):
        cutomer_no = str(post.get('cutomer_no'))
        first_name = str(post.get('first_name'))
        last_name = str(post.get('last_name'))
        street = str(post.get('street'))
        city = str(post.get('city'))
        country = str(post.get('country'))
        dob = str(post.get('dob'))
        proof_id = str(post.get('proof_id'))
        security_no = str(post.get('security_no'))
        employer_name = str(post.get('employer_name'))
        employer_income = str(post.get('employer_income'))
        account_no = str(post.get('account_no'))
        ifsc_code = str(post.get('ifsc_code'))
        notes = str(post.get('notes'))

        vals = {'cutomer_no':cutomer_no,'first_name':first_name,'last_name':last_name,
                'street':street,'city':city,'country':country,'dob':dob,'proof_id':proof_id,
                'security_no':security_no,'employer_name':employer_name,'employer_income':employer_income,
                'account_no':account_no,'ifsc_code':ifsc_code,'notes':notes}

        new_rec = request.env['emp.inquiry'].create(vals)

        print ('\n\n\n new_rec----------------------->',new_rec)

        return ('THANKS FOR INQUIRY.')