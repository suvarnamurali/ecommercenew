function c_validation(){

    alert('hello')  
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
// seller validation 
// function s_validation(){
//     alert('haiii')
//   var sname =  document.getElementById('rs_name').value
//   var address = document.getElementById('rs_address').value
//   var email = document.getElementById('rs_mail').value
//   var acholder = document.getElementById('rs_acholder').value
//   var accountno = document.getElementById('rs_ac_no').value
//   var ifsc = document.getElementById('rs_ifsc').value
 
//   var password = document.getElementById('rs_password').value
//   var email_pattern = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"

//   if (sname == ''){
      
//       document.getElementById('name_rs').innerHTML ='Please fill out this field' /*span id name_rs */
//       document.getElementById('rs_name').style.borderBottom='1px solid red'
//       document.getElementById('name_rs').style.color ='red'
//       return false

//   }
//   else{
//       document.getElementById('name_rs').innerHTML =''
//       document.getElementById('rs_name').style.color ='blue 1px solid'
//       return false
//   }
//   if (address == ''){
//       document.getElementById('address_rs').innerHTML ='Please fill out this field' /*span id address_rs */
//       document.getElementById('rs_address').style.borderBottom='1px solid red'
//       document.getElementById('address_rs').style.color ='red'
//       return false
//   }
//   else{
//       document.getElementById('address_rs').innerHTML =''
//       document.getElementById('rs_address').style.color ='blue 1px solid'
//       return false
//   }
//   if (email == ''){
     
//       document.getElementById('mail_rs').innerHTML ='Please fill out this field'/*span id mail_rs */
//       document.getElementById('rs_mail').style.borderBottom='1px solid red'
//       document.getElementById('mail_rs').style.color ='red'
//       return false
//   }
//   else{
//       document.getElementById('mail_rs').innerHTML =''
//       document.getElementById('rs_mail').style.color ='blue 1px solid'
//       if (email_pattern == null()){
//           document.getElementById('mail_rs').innerHTML ='email pattern incorrect'/*check */
//           return false
//       }
//   }
//   if (acholder == ''){
//       document.getElementById('acholder_rs').innerHTML ='Please fill out this field' /*span id acholder_rs */
//       document.getElementById('rs_acholder').style.borderBottom='1px solid red'
//       document.getElementById('acholder_rs').style.color ='red'
//       return false

//   }
//   else{
//       document.getElementById('acholder_rs').innerHTML =''
//       document.getElementById('rs_acholder').style.color ='blue 1px solid'
//       return false
//   }
//   if (accountno == ''){
//       document.getElementById('ac_no_rs').innerHTML ='Please fill out this field' /*span id ac_no_rs */
//       document.getElementById('rs_ac_no').style.borderBottom='1px solid red'
//       document.getElementById('ac_no_rs').style.color ='red'
//       return false
//   }
//   else{
//       document.getElementById('ac_no_rs').innerHTML =''
//       document.getElementById('rs_ac_no').style.color ='blue 1px solid'
//       return false
//   }
//   if (ifsc == ''){
//       document.getElementById('ifsc_rs').innerHTML ='Please fill out this field' /*span id ifsc_rs */
//       document.getElementById('rs_ifsc').style.borderBottom='1px solid red'
//       document.getElementById('ifsc_rs').style.color ='red'
//       return false
//   }
//   else{
//       document.getElementById('ifsc_rs').innerHTML =''
//       document.getElementById('rs_ifsc').style.color ='blue 1px solid'
//       return false
//   }
//   if (password == ''){
      
//       document.getElementById('password_rs').innerHTML ='Please fill out this field' /*span id password_rs */
//       document.getElementById('rs_password').style.borderBottom='1px solid red'
//       document.getElementById('password_rs').style.color ='red'
//       return false

//   }
//   else{
//       document.getElementById('password_rs').innerHTML =''
//       document.getElementById('rs_password').style.color ='blue 1px solid'
//       return false
//   }


// }