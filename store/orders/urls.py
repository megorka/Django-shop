from django.urls import path
from orders.views import order_create, order_success, orders, order
app_name = 'orders'

urlpatterns = [
    path('order-create/', order_create, name='order-create'),
    path('success', order_success, name='success'),
    path('orders', orders, name='orders'),
    path('order/<int:order_id>/', order, name='order'),
]
