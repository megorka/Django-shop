from django.urls import path, include
from products.views import products, basket_add

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add')
]