from django.shortcuts import render, HttpResponseRedirect
from products.models import Basket, Product
from orders.models import OrderItem, Order
from orders.forms import OrderCreateForm
from django.urls import reverse


def order_create(request):
    baskets = Basket.objects.filter(user=request.user)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()
            for basket in baskets:
                OrderItem.objects.create(
                    order=order,
                    product=basket.product,
                    price=basket.product.price,
                    quantity=basket.quantity
                )
            baskets.delete()
            return HttpResponseRedirect(reverse('products:index'))
    else:
        form = OrderCreateForm()

    context = {
        'baskets': baskets,
        'form': form
    }
    return render(request, 'orders/order-create.html', context)
