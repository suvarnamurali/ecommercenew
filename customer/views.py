from django.shortcuts import render

# Create your views here.

def customer_home(request):
    return render(request,'customer/customer_home.html')

def my_cart(request):
    return render(request,'customer/my_cart.html')

def my_order(request):
    return render(request,'customer/my_orders.html')

def product_detail(request):
    return render(request,'customer/product_detail.html')
