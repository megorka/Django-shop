from django.db import models
from products.models import Product
from users.models import AbstractUser


class Order(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=256)

    def __str__(self):
        return f'Заказ номер: {self.id}'

    def total_sum(self):
        return sum(basket.sum() for basket in AbstractUser)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
