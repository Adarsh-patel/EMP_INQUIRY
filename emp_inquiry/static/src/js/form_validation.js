odoo.define('emp_inquiry.Form_validation',function(){

    $(document).ready(function(){
        $("input").focus(function(){
            $(this).css('border','2px solid red')
        });
    });
});