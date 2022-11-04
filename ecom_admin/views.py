from django.shortcuts import render

from reseller_app.models import Reseller

# Create your views here.

def admin_home(request):
    return render(request,'ecom_admin/admin_home.html')

def approve_resellers(request):
    reseller = Reseller.objects.filter(reseller_id = request.session['s_id'])
    return render(request,'ecom_admin/approve_resellers.html',{'reseller_list':reseller})

def customers_list(request):
    return render(request,'ecom_admin/customers_list.html')

def registered_resellers(request):
    return render(request,'ecom_admin/registered_resellers.html')

def change_password(request):
    return render(request,'ecom_admin/change_password.html')

def admin_login(request):
    return render(request,'ecom_admin/adminlogin.html')





