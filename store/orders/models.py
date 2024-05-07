from django.db import models
from products.models import Product
from users.models import User


class Order(models.Model):
    STATUS_CHOICES = (
        ('paid', 'Оплачено'),
        ('delivered', 'Доставлено'),
        ('in_route', 'В пути')
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paid')

    def __str__(self):
        return f'Заказ номер: {self.id}'

    def total_price(self):
        return sum(item.get_price() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_price(self):
        return self.price * self.quantity
