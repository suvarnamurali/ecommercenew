 
from itertools import product
from urllib import request
from django.shortcuts import render,redirect

from customer.models import AddCart, Customer
from reseller_app.models import Product, Reseller
# from django.db.models import F,Sum

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

            customer = Customer(
                first_name = first_name,
                last_name =second_name,
                email = e_mail,
                 mobile = c_phone,
                 password = c_password)
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
                return redirect("reseller:reseller_home")
            except:
                error_msg = 'Invalid Username Or Password'
                return render(request,'customer/customer_home.html',{'error_msg':error_msg}) 
                   
    product_list=Product.objects.all() 
    return render(request,'customer/customer_home.html',{'products':product_list})
    return render(request,'customer/customer_home.html',{'status':status})

# def my_cart(request,product_id):
#     msg=""
#     if 'c_id' not in request.session: 
#         msg="plase login"       
#         product_detail=Product.objects.get(id=product_id)
#         return render(request,'customer/product_detail.html',{'product':product_detail,'error':msg})
#     else:        
#         cart = AddCart(
#             product_id = product_id ,
#             customer_id = request.session['c_id'])

#         product_exist=AddCart.objects.filter(product_id=product_id).exists()
#         if not product_exist:
#             cart.save()
#     return redirect('customer:view_cart') 


def my_cart(request):
    # msg=""
    # if request.method == "POST":
    #     p_id=request.POST['pid']
    #     p_qty=request.POST['qty'] 
        
    #     cart = AddCart(
    #     product_id = p_id ,
    #     qty=p_qty,
    #     customer_id = request.session['c_id'])

    #     if 'c_id' not in request.session: 
    #         msg="plase login"    
    #         return render(request,'customer/product_detail.html',{'product':product_detail,'error':msg})
    #     else:  
    #         product_exist=AddCart.objects.filter(product_id=p_id).exists()
    #         if not product_exist:
    #             cart.save()
    return redirect('customer:view_cart') 


def view_cart(request):
    #cart_sum = Cart.objects.filter(user=request.user).aggregate(total_price=Sum('item__price', field='item__price * number_of_items')).get('total_price')
    cart_items1 = AddCart.objects.filter(customer_id=request.session['c_id']).aaggregate(tt_price=sum('product.p_price' , field='product.p_price * qty')) 
    #cart_items =AddCart.objects.annotate(total_price=sum(F('product.p_price') * F('qty')).get(customer_id=request.session['c_id']))
    # t_price = []
    # for item in cart_items1:
    #     price = item.product.p_price * item.qty
    #     t_price.append(price)
    

    return render(request,'customer/my_cart.html',{'cart_items':cart_items1,})

def del_cart_item(reqest,product_id):
    del_item=AddCart.objects.get(product_id=product_id)
    del_item.delete()
    return redirect('customer:view_cart') 

def my_order(request):
    return render(request,'customer/my_orders.html')

def product_detail(request,product_id):
    if request.method == "POST":
        p_id=request.POST['pid']
        p_qty=request.POST['qty'] 
        
        cart = AddCart(
        product_id = p_id ,
        qty=p_qty,
        customer_id = request.session['c_id'])

        if 'c_id' not in request.session: 
            msg="plase login"    
            return render(request,'customer/product_detail.html',{'product':product_detail,'error':msg})
        else:  
            product_exist=AddCart.objects.filter(product_id=p_id).exists()
            if not product_exist:
                cart.save()
            
        return redirect('customer:view_cart')


    product_detail=Product.objects.get(id=product_id)
    return render(request,'customer/product_detail.html',{'product':product_detail})


def my_ac(request):
    customer_P=Customer.objects.get(id=request.session['c_id']) #select * from table where     
    return render(request,'customer/my_account.html',{'customer_details':customer_P})

def edit_form(request):
    return render(request,'customer/editform.html')

def c_address(request):
    return render(request,'customer/address.html')

def c_payment(request):
    return render(request,'customer/payment.html')

def c_logout(request):
    del request.session['c_id']
    request.session.flush()
    return redirect('customer:home')

