from django.shortcuts import render

from reseller_app.models import Reseller

# Create your views here.

def reseller_home(request):
    reseller = Reseller.objects.get(id = request.session['s_id'])
    return render(request,'reseller_app/reseller_home.html',{'seller_data':reseller})

def product_catalogue(request):
    return render(request,'reseller_app/catalogue.html')

def add_product(request):
    return render(request,'reseller_app/add_product.html')

def my_order(request):
    return render(request,'reseller_app/my_orders.html')

def update_stock(request):
    return render(request,'reseller_app/update_stock.html')

def recent_orders(request):
    return render(request,'reseller_app/recent_orders.html')

def cancelled_orders(request):
    return render(request,'reseller_app/cancelled_orders.html')

def order_history(request):
    return render(request,'reseller_app/order_history.html')

def change_password(request):
    return render(request,'reseller_app/change_password.html')

def seller_ac(request):
    return render(request,'reseller_app/seller_account.html')

def edit_ac(request):
    return render(request,'reseller_app/s_edit.html')

 
 


