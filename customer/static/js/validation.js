function c_validation(){

    var address = document.getElementById('c_address').value
    var email = document.getElementById('c_mail').value
    var password = document.getElementById('c_pass').value
    var email_pattern = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
    var password_pattern = "/^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9]{7,}$/"

    if (address == ''){
        document.getElementById('c_add').innerHTML ='Please fill out this field' /*span id c_add */
        document.getElementById('c_address').style.borderBottom='1px solid red'
        document.getElementById('c_add').style.color ='red'

    }
    else{
        document.getElementById('c_add').innerHTML =''
    }
    if (email == ''){
       
        document.getElementById('mail_c').innerHTML ='Please fill out this field'/*span id mail_c */
        document.getElementById('c_mail').style.borderBottom='1px solid red'
        document.getElementById('mail_c').style.color ='red'
        
    }
    else{
        document.getElementById('mail_c').innerHTML =''
        document.getElementById('c_mail').style.color ='blue 1px solid'
        if (email_pattern == null()){
            document.getElementById('mail_c').innerHTML ='email pattern incorrect'/*check */
        }
    }
    if (password == ''){
        
        document.getElementById('c_pswd').innerHTML ='Please fill out this field'/*span id c_pswd*/
        document.getElementById('c_pass').style.borderBottom ='red 1px solid'
        document.getElementById('c_pswd').style.color ='red'
        
    }
    else{
        document.getElementById('c_pswd').innerHTML =''
        document.getElementById('c_pass').style.color ='blue 1px solid'
    }
}