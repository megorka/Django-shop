from django.urls import path
from orders.views import order_create, order_success, orders
app_name = 'orders'

urlpatterns = [
    path('order-create/', order_create, name='order'),
    path('success', order_success, name='success'),
    path('orders', orders, name='orders'),
]