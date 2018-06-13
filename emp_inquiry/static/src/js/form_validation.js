odoo.define('emp_inquiry.Form_validation',function(require){

    $(document).ready(function(){
        $("input").focus(function(){
            $(this).css('border','2px solid Blue');
        });
        $("#customer_no").focusout(function(){

            var customer_no=$('#customer_no').val();
            console.log('before if cust-_no',customer_no.length);
            if($.isNumeric(customer_no)){
                $(this).css('border','2px solid #ccc');
            }
            else{
                console.log('after if cust-_no',customer_no);
                $(this).css('border','2px solid red');
            }
        });
        $("#first_name").keypress(function(e){
            var first_name=$('#first_name').val();
            console.log('before if first_name',first_name);
            if(e.keyCode >= 65 && e.keyCode <= 90 || e.keyCode >= 97 && e.keyCode <= 122 || e.keyCode == 32 || e.keyCode == 9){
                console.log('after if first_name',first_name);
                $(this).css('border','2px solid #ccc');
            }
            else{
                e.preventDefault();
            }
        });
        $("#first_name").focusout(function(){
            var first_name=$('#first_name').val();
            if (first_name.length < 1){
                $(this).css('border','2px solid red');
            }
        });
        $("#last_name").keypress(function(e){
            var last_name=$('#last_name').val();
            console.log('before if last_name',last_name);
            if(e.keyCode >= 65 && e.keyCode <= 90 || e.keyCode >= 97 && e.keyCode <= 122 || e.keyCode == 32 || e.keyCode == 9){
                console.log('after if last_name',last_name);
                $(this).css('border','2px solid #ccc');
            }
            else{
                e.preventDefault();
            }
        });
        $("#last_name").focusout(function(){
            var last_name=$('#last_name').val();
            if (last_name.length < 1){
                $(this).css('border','2px solid red');
            }
        });
        $("#street").focusout(function(){
            var street=$('#street').val();
            console.log('street',street.length);
            if(street.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });
        $("#city").focusout(function(){
            var city=$('#city').val();
            console.log('city',city.length);
            if(city.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });
        $("#country").focusout(function(){
            var country=$('#country').val();
            console.log('country',country.length);
            if(country.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });
        $("#dob").focusout(function(){
            var dob=$('#dob').val();
            console.log('dob',dob.length);
            if(dob.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });
        $("#proof_id").focusout(function(){
            var proof_id=$('#proof_id').val();
            console.log('proof_id',proof_id.length);
            if(proof_id.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });

        $("#security_no1").keypress(function(e){
            var security_no1=$('#security_no1').val();
            console.log('before if security_no1',security_no1.length);
            if(e.keyCode >= 48 && e.keyCode <= 57){
                console.log('after if security_no1',security_no1);
                $(this).css('border','2px solid #ccc');
            }
            else{
                e.preventDefault();
            }
        });
        $("#security_no2").keypress(function(e){
            var security_no2=$('#security_no2').val();
            console.log('before if security_no2',security_no2.length);
            if(e.keyCode >= 48 && e.keyCode <= 57){
                console.log('after if security_no2',security_no2);
                $(this).css('border','2px solid #ccc');
            }
            else{
                e.preventDefault();
            }
        });
        $("#security_no3").keypress(function(e){
            var security_no3=$('#security_no3').val();
            console.log('before if security_no3',security_no3.length);
            if(e.keyCode >= 48 && e.keyCode <= 57){
                console.log('after if security_no3',security_no3);
                $(this).css('border','2px solid #ccc');
            }
            else{
                e.preventDefault();
            }
        });
        $("#security_no1").focusout(function(){
            var security_no1=$('#security_no1').val();
            if (security_no1.length < 1){
                $(this).css('border','2px solid red');
            }
        });
        $("#security_no2").focusout(function(){
            var security_no2=$('#security_no2').val();
            if (security_no2.length < 1){
                $(this).css('border','2px solid red');
            }
        });
        $("#security_no3").focusout(function(){
            var security_no3=$('#security_no3').val();
            if (security_no3.length < 1){
                $(this).css('border','2px solid red');
            }
        });
        $("#employer_name").focusout(function(){
            var employer_name=$('#employer_name').val();
            console.log('employer_name',employer_name.length);
            if(employer_name.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });
        $("#employer_income").keypress(function(e){
            var employer_income=$('#employer_income').val();
            console.log('before if employer_income',employer_income.length);
            if(e.keyCode >= 48 && e.keyCode <= 57){
                console.log('after if first_name',first_name);
                $(this).css('border','2px solid #ccc');
            }
            else{
                e.preventDefault();
            }
        });
        $("#employer_income").focusout(function(){
            var employer_income=$('#employer_income').val();
            if (employer_income.length < 1){
                $(this).css('border','2px solid red');
            }
        });
        $("#account_no").keypress(function(e){
            var account_no=$('#account_no').val();
            console.log('before if account_no',account_no.length);
            if(e.keyCode >= 48 && e.keyCode <= 57){
                console.log('after if first_name',first_name);
                $(this).css('border','2px solid #ccc');
            }
            else{
                e.preventDefault();
            }
        });
        $("#account_no").focusout(function(){
            var account_no=$('#account_no').val();
            if (account_no.length < 1){
                $(this).css('border','2px solid red');
            }
        });
        $("#ifsc_code").focusout(function(){
            var ifsc_code=$('#ifsc_code').val();
            console.log('ifsc_code',ifsc_code.length);
            if(ifsc_code.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });
        $("#notes").focusout(function(){
            var notes=$('#notes').val();
            console.log('notes',notes.length);
            if(notes.length < 1){
                $(this).css('border','2px solid red');
            }else{
                $(this).css('border','2px solid #ccc');
            }
        });

        function movefocus(from, to){
            var len = from.val.length;
            console.log("hello testing length",len)
        }

    });
});