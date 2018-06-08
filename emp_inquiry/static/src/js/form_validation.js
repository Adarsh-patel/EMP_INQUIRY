odoo.define('emp_inquiry.Form_validation',function(){

    $(document).ready(function(){
        $("input").change(function(){
            $(this).css('border','2px solid red')
        });
    });
});