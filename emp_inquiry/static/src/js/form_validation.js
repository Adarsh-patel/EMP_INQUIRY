odoo.define('emp_inquiry.Form_validation',function(require){

    $(document).ready(function(){
        $("input").focus(function(){
            $(this).css('border','2px solid Blue');
        });
        $("#customer_no").focusout(function(){
            var format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
            var customer_no=$('#customer_no').val();
            var last_name=$('#last_name').val();
            console.log('before if',customer_no.length);
//            console.log('answer--->',$.isNumeric(name1));
            if($.isNumeric(customer_no)){
                $(this).css('border','2px solid #ccc');
            }
            else{
                console.log('after if',customer_no,$.isNumeric(customer_no));
                $(this).css('border','2px solid red');
            }
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
        $("#last_name").focusout(function(){
            var format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
            var last_name=$('#last_name').val();
            var last_name=$('#last_name').val();
            console.log('before if',last_name.length);
//            console.log('answer--->',$.isNumeric(name1));
            if($.isNumeric(last_name) || format.test(last_name) || last_name.length == 0){
                console.log('after if',last_name,$.isNumeric(last_name),format.test(last_name),last_name.length == 0);
                $(this).css('border','2px solid red');
            }
            else{
                $(this).css('border','2px solid #ccc');
            }
        });
        $("#street").focusout(function(){
            var street=$('#street').val();
            console.log('before if',street.length);
            $(this).css('border','2px solid #ccc');
        });
        $("#city").focusout(function(){
            var city=$('#city').val();
            console.log('before if',city.length);
            $(this).css('border','2px solid #ccc');
        });
        $("#employer_income").focusout(function(){
            var format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
            var employer_income=$('#employer_income').val();
            var last_name=$('#last_name').val();
            console.log('before if',employer_income.length);
//            console.log('answer--->',$.isNumeric(name1));
            if($.isNumeric(employer_income)){
                console.log('after if',employer_income,$.isNumeric(employer_income));
                $(this).css('border','2px solid #ccc');
            }
            else{
                console.log('after if',employer_income,$.isNumeric(employer_income));
                $(this).css('border','2px solid red');
            }
        });
    });
});