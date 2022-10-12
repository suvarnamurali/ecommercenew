from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render(request,'ecom_admin/admin_home.html')

def approve_resellers(request):
    return render(request,'ecom_admin/approve_resellers.html')

def customers_list(request):
    return render(request,'ecom_admin/customers_list.html')

def registered_resellers(request):
    return render(request,'ecom_admin/registered_resellers.html')

def change_password(request):
    return render(request,'ecom_admin/change_password.html')





