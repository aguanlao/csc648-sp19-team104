counter0 = counter1 = counter2 = counter3 = 0;
counter4 = counter5 = counter6 = counter7 = 0;
counter8 = counter9 = counter10 = counter11= 0;


$('#defaultCheckid_first_name').click(function(){
    if (counter0 == 1) {
        $('#id_first_name').prop('readonly', true);
        counter0 -=1;
    } else {
        $('#id_first_name').prop('readonly', false);
        counter0 +=1;
    }      
});    

$('#defaultCheckid_last_name').click(function(){
    if (counter1 == 1) {
        $('#id_last_name').prop('readonly', true);
        counter1 -=1;
    } else {
        $('#id_last_name').prop('readonly', false);
        counter1 +=1;
    }      
});       

$('#defaultCheckid_date_of_birth').click(function(){
    if (counter2 == 1) {
        $('#id_date_of_birth').prop('readonly', true);
        counter2 -=1;
    } else {
        $('#id_date_of_birth').prop('readonly', false);
        counter2 +=1;
    }      
});       

$('#defaultCheckid_physical_address').click(function(){
    if (counter3 == 1) {
        $('#id_physical_address').prop('readonly', true);
        counter3 -=1;
    } else {
        $('#id_physical_address').prop('readonly', false);
        counter3 +=1;
    }      
});     

$('#defaultCheckid_city').click(function(){
    if (counter4 == 1) {
        $('#id_city').prop('readonly', true);
        counter4 -=1;
    } else {
        $('#id_city').prop('readonly', false);
        counter4 +=1;
    }      
});  

$('#defaultCheckid_state').click(function(){
    if (counter5 == 1) {
        $('#id_state').prop('readonly', true);
        counter5 -=1;
    } else {
        $('#id_state').prop('readonly', false);
        counter5 +=1;
    }      
}); 

$('#defaultCheckid_zip_code').click(function(){
    if (counter6 == 1) {
        $('#id_zip_code').prop('readonly', true);
        counter6 -=1;
    } else {
        $('#id_zip_code').prop('readonly', false);
        counter6 +=1;
    }      
}); 

$('#defaultCheckid_phone_number').click(function(){
    if (counter7 == 1) {
        $('#id_phone_number').prop('readonly', true);
        counter7 -=1;
    } else {
        $('#id_phone_number').prop('readonly', false);
        counter7 +=1;
    }      
});

$('#defaultCheckid_email').click(function(){
    if (counter8 == 1) {
        $('#id_email').prop('readonly', true);
        counter8 -=1;
    } else {
        $('#id_email').prop('readonly', false);
        counter8 +=1;
    }      
}); 

$('#defaultCheckid_username').click(function(){
    if (counter9 == 1) {
        $('#id_username').prop('readonly', true);
        counter9 -=1;
    } else {
        $('#id_username').prop('readonly', false);
        counter9 +=1;
    }      
});

$('#defaultCheckid_bio').click(function(){
    if (counter10 == 1) {
        $('#id_bio').prop('readonly', true);
        counter10 -=1;
    } else {
        $('#id_bio').prop('readonly', false);
        counter10 +=1;
    }
});

$('#defaultCheckid_profile_picture').click(function(){
    if (counter11 == 1) {
        $('#id_profile_picture').prop('readonly', true);
        counter11 -=1;
    } else {
        $('#id_profile_picture').prop('readonly', false);
        counter11 +=1;
    }
});

