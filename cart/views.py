from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from decimal import Decimal
from product.models import ProductRegister
from django.conf import settings
from.cart import Cart

# Create your views here.


def cartView(request, mode):
    product_list = ProductRegister.objects.all()

    modes = ['Sale', 'Purchase', 'Rent']
    if mode not in modes:
        raise Http404

    for product in product_list:
        if mode == 'Sale':
            product.price = product.productBrandNewSellingRate
        elif mode == 'Rent':
            product.price = product.productDailyRentalRate
        elif mode == 'Purchase':
            product.price = product.productBrandNewSellingRate
        else:
            product.price = 0

    cart = Cart(request, mode)
    context = {'mode': mode, }
    # print(cart.cart)
    print(cart.mode)
    if cart.mode != mode:
        error = f'Error !! Your {cart.mode} cart is not empty . Clear it to use {mode} cart'
        context['error'] = error

    if request.GET:
        if request.GET['action'] == 'add':
            product_id = request.GET['id']
            match = get_object_or_404(ProductRegister, id=product_id)
            for product in product_list:
                if product.id == match.id:
                    cart.add(product=match, price=product.price)
            return redirect('cart_view', mode=mode)

        if request.GET['action'] == 'remove':
            product_id = request.GET['id']
            product = get_object_or_404(ProductRegister, id=product_id)
            cart.remove(product=product)
            return redirect('cart_view', mode=mode)

        if request.GET['action'] == 'clear':
            cart.clear()
            return redirect('cart_view', mode=mode)

    if request.POST:
        if request.POST['submit'] == 'update':
            product_ids = cart.cart.keys()
            for product_id in product_ids:
                update_value = int(request.POST[product_id])
                cart.update(product_id=product_id, update_value=update_value)
            return redirect('cart_view', mode=mode)

        if request.POST['submit'] == 'checkout':
            product_ids = cart.cart.keys()
            for product_id in product_ids:
                update_value = int(request.POST[product_id])
                cart.update(product_id=product_id, update_value=update_value)
            return redirect('order_confirm_quotation', mode=mode)

    context['product_list'] = product_list
    context['cart'] = cart
    return render(request, 'cart/cart_view.html', context)
