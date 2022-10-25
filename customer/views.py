 
from django.shortcuts import render

from customer.models import Customer
from reseller_app.models import Reseller

# Create your views here.

def customer_home(request):
    status = ""
    if request.method =='GET':
        status = False
    if request.method == 'POST':
        if 'c_signup' in request.POST:
            first_name = request.POST['fname']
            second_name = request.POST['sname']
            e_mail = request.POST['c_email']
            c_phone = request.POST['c_phno']
            c_password = request.POST['c_passwd']

            customer = Customer(first_name = first_name,last_name =second_name,email = e_mail, mobile = c_phone,password = c_password)
            customer.save()

        if 'c_login' in request.POST:
            email = request.POST['c_user_id']
            passwd = request.POST['c_user_passwd']

            try:
                customer = Customer.objects.get(email = email,password = passwd)
                request.session['c_id'] = customer.id
                print('testt')
                 
            except:
                error_msg = 'Invalid Username Or Password'
                return render(request,'customer/customer_home.html',{'error_msg':error_msg})#customer end
     
   
        if 's_signup' in request.POST:
            s_name = request.POST['s_name']
            s_email = request.POST['s_email']
            s_mobile = request.POST['s_mobile']
            s_address = request.POST['s_address']
            s_account = request.POST['s_account']
            s_ifsc = request.POST['s_ifsc']
            s_acholder = request.POST['s_acholder']
            s_password = request.POST['s_password']
            s_pic = request.POST['s_pic']

            reseller = Reseller(s_name = s_name,email = s_email,mobile = s_mobile,address = s_address,account_no =s_account,ifsc = s_ifsc,
            s_acholdername = s_acholder,password = s_password,s_pic = s_pic)
            reseller.save()

        if 'signin' in request.POST:
            email = request.POST['s_mail']
            passwd = request.POST['s_pass']
            print('seller')

            try:
                reseller = Reseller.objects.get(email = email,password = passwd)
                request.session['s_id'] = reseller.id
               
                 
            except:
                error_msg = 'Invalid Username Or Password'
                return render(request,'reseller/reseller_home.html',{'error_msg':error_msg})
        

    return render(request,'customer/customer_home.html',{'status':status})

def my_cart(request):
    return render(request,'customer/my_cart.html')

def my_order(request):
    return render(request,'customer/my_orders.html')

def product_detail(request):
    return render(request,'customer/product_detail.html')

def my_ac(request):
    return render(request,'customer/my_account.html')

def edit_form(request):
    return render(request,'customer/editform.html')

def c_address(request):
    return render(request,'customer/address.html')

def c_payment(request):
    return render(request,'customer/payment.html')

