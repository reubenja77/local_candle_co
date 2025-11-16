from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product

CART_SESSION_KEY = 'cart'


def _get_cart(request):
    """
    Return the cart dictionary from the session.
    Keys are product IDs (as strings), values are quantities.
    """
    return request.session.setdefault(CART_SESSION_KEY, {})


def cart_view(request):
    cart = _get_cart(request)
    items = []
    total = Decimal('0.00')

    for pid, qty in cart.items():
        product = get_object_or_404(Product, id=int(pid), is_active=True)
        line_total = Decimal(qty) * product.price
        items.append({
            'product': product,
            'qty': qty,
            'line_total': line_total,
        })
        total += line_total

    return render(request, 'checkout/cart.html', {'items': items, 'total': total})


def cart_add(request, product_id):
    cart = _get_cart(request)
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session.modified = True

    product = get_object_or_404(Product, id=product_id)
    messages.success(request, 'Added to cart.')
    return redirect('products:detail', slug=product.slug)


def cart_remove(request, product_id):
    cart = _get_cart(request)
    cart.pop(str(product_id), None)
    request.session.modified = True

    messages.info(request, 'Removed from cart.')
    return redirect('checkout:cart')