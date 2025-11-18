from decimal import Decimal

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from products.models import Product

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def cart_view(request):
    """
    Show the current cart contents.
    """
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    items = []
    total = Decimal('0.00')

    for product in products:
        qty = cart.get(str(product.id), 0)
        subtotal = product.price * qty
        total += subtotal
        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal,
        })

    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'checkout/cart.html', context)


def cart_add(request, product_id):
    """
    Add a product to the cart stored in the session.
    """
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart

    # After adding, send user to cart page
    return redirect('checkout:cart')


def cart_remove(request, product_id):
    """
    Remove a product from the cart stored in the session.
    """
    cart = request.session.get('cart', {})
    key = str(product_id)

    if key in cart:
        del cart[key]
        request.session['cart'] = cart

    return redirect('checkout:cart')


def checkout_view(request):
    """
    Checkout page:
    - Reads cart from session
    - Calculates total
    - Creates a Stripe PaymentIntent
    - Sends stripe_public_key and client_secret to the template
    """
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    items = []
    total = Decimal('0.00')

    for product in products:
        qty = cart.get(str(product.id), 0)
        subtotal = product.price * qty
        total += subtotal
        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal,
        })

    # If cart is empty, show checkout page without intent
    if total <= 0:
        return render(request, 'checkout/checkout.html', {
            'items': [],
            'total': total,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': None,
        })

    # Create Stripe PaymentIntent (amount in cents)
    intent = stripe.PaymentIntent.create(
        amount=int(total * 100),
        currency='zar',
        metadata={
            'integration_check': 'accept_a_payment',
        }
    )

    context = {
        'items': items,
        'total': total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def success(request):
    """
    Clear the cart and show success page.
    """
    request.session['cart'] = {}
    return render(request, 'checkout/success.html')


def error(request):
    """
    Simple error page for failed payments.
    """
    return render(request, 'checkout/error.html')