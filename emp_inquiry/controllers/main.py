from odoo import http
from odoo.http import request

class inquiry_from(http.Controller):

    @http.route('/emp/inquiry',type='http',auth='public',website='True')
    def emp_form(self):
        print('\n\n\n Hello Website')
        return request.render('emp_inquiry.emp_form')