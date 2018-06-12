odoo.define('emp_inquiry.Form_validation',function(require){

    $(document).ready(function(){
        $("input").focus(function(){
            $(this).css('border','2px solid Blue');
        });
        $("#first_name").focusout(function(){
            var format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
            var first_name=$('#first_name').val();
            var last_name=$('#last_name').val();
            console.log('before if',first_name.length);
//            console.log('answer--->',$.isNumeric(name1));
            if($.isNumeric(first_name) || format.test(first_name) || first_name.length == 0){
                console.log('after if',first_name,$.isNumeric(first_name),format.test(first_name),first_name.length == 0);
                $(this).css('border','2px solid red');
            }
            else{
                $(this).css('border','2px solid #ccc');
            }
        });
    });
});