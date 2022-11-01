from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('',views.customer_home,name='home'),
    path('my-cart',views.my_cart, name='cart'),
    path('my-order',views.my_order, name='order'),
    path('p-detail',views.product_detail, name='product_detail'),
    path('myaccount',views.my_ac, name='my-account'),
    path('edit',views.edit_form, name='my-edit'),
    path('add_ress',views.c_address, name='address_c'),
    path('pay_ment',views.c_payment, name='payment_c'),
    path('log_out',views.logout,name='log_out'),
    path('logout_s',views.log_out,name='logout_s')
    
]