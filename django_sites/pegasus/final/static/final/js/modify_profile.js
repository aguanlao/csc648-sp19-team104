counter0 = counter1 = counter2 = counter3 = 0;
counter4 = counter5 = counter6 = counter7 = 0;
counter8 = counter9 = counter10 = counter11= 0;


$('#defaultCheckid_first_name').click(function(){
    if (counter0 == 1) {
        $('#id_first_name').attr('disabled','disabled');
        counter0 -=1;
    } else {
        $('#id_first_name').removeAttr('disabled','disabled');
        counter0 +=1;
    }      
});    

$('#defaultCheckid_last_name').click(function(){
    if (counter1 == 1) {
        $('#id_last_name').attr('disabled','disabled');
        counter1 -=1;
    } else {
        $('#id_last_name').removeAttr('disabled','disabled');
        counter1 +=1;
    }      
});       

$('#defaultCheckid_date_of_birth').click(function(){
    if (counter2 == 1) {
        $('#id_date_of_birth').attr('disabled','disabled');
        counter2 -=1;
    } else {
        $('#id_date_of_birth').removeAttr('disabled','disabled');
        counter2 +=1;
    }      
});       

$('#defaultCheckid_physical_address').click(function(){
    if (counter3 == 1) {
        $('#id_physical_address').attr('disabled','disabled');
        counter3 -=1;
    } else {
        $('#id_physical_address').removeAttr('disabled','disabled');
        counter3 +=1;
    }      
});     

$('#defaultCheckid_city').click(function(){
    if (counter4 == 1) {
        $('#id_city').attr('disabled','disabled');
        counter4 -=1;
    } else {
        $('#id_city').removeAttr('disabled','disabled');
        counter4 +=1;
    }      
});  

$('#defaultCheckid_state').click(function(){
    if (counter5 == 1) {
        $('#id_state').attr('disabled','disabled');
        counter5 -=1;
    } else {
        $('#id_state').removeAttr('disabled','disabled');
        counter5 +=1;
    }      
}); 

$('#defaultCheckid_zip_code').click(function(){
    if (counter6 == 1) {
        $('#id_zip_code').attr('disabled','disabled');
        counter6 -=1;
    } else {
        $('#id_zip_code').removeAttr('disabled','disabled');
        counter6 +=1;
    }      
}); 

$('#defaultCheckid_phone_number').click(function(){
    if (counter7 == 1) {
        $('#id_phone_number').attr('disabled','disabled');
        counter7 -=1;
    } else {
        $('#id_phone_number').removeAttr('disabled','disabled');
        counter7 +=1;
    }      
}); 

$('#defaultCheckid_email').click(function(){
    if (counter8 == 1) {
        $('#id_email').attr('disabled','disabled');
        counter8 -=1;
    } else {
        $('#id_email').removeAttr('disabled','disabled');
        counter8 +=1;
    }      
}); 

$('#defaultCheckid_username').click(function(){
    if (counter9 == 1) {
        $('#id_username').attr('disabled','disabled');
        counter9 -=1;
    } else {
        $('#id_username').removeAttr('disabled','disabled');
        counter9 +=1;
    }      
}); 

