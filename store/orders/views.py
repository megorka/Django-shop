from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from products.models import Basket
from orders.models import OrderItem, Order
from orders.forms import OrderCreateForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
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


@login_required
def order_success(request):
    return render(request, 'orders/success.html')


@login_required
def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {
        'orders': order
    }
    return render(request, 'orders/orders.html', context)

@login_required
def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    orders = Order.objects.filter(id=order_id)
    products = order.items.all()
    context = {
        'orders': orders,
        'products': products
    }
    return render(request, 'orders/order.html', context)
