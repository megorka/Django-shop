from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdm(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'created', 'updated', 'status']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]
