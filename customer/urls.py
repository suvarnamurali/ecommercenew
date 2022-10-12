from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('',views.customer_home,name='home'),
    path('my-cart',views.my_cart, name='cart'),
    path('my-order',views.my_order, name='order'),
    path('p-detail',views.product_detail, name='product_detail')
]