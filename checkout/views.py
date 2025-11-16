from decimal import Decimal

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

import stripe

from products.models import Product
from .forms import CheckoutForm
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

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


def checkout_view(request):
    """
    Simple checkout:
    - Uses cart total
    - Creates Stripe PaymentIntent
    - Creates Order with status 'paid'
    - Clears cart
    """
    cart = _get_cart(request)
    if not cart:
        messages.info(request, 'Your cart is empty.')
        return redirect('products:list')

    # calculate total
    total = Decimal('0.00')
    for pid, qty in cart.items():
        product = get_object_or_404(Product, id=int(pid), is_active=True)
        total += Decimal(qty) * product.price

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                # Create a PaymentIntent on Stripe (test keys)
                intent = stripe.PaymentIntent.create(
                    amount=int(total * 100),  # convert to cents
                    currency=settings.STRIPE_CURRENCY,
                    metadata={'integration_check': 'accept_a_payment'},
                )
            except stripe.error.StripeError:
                messages.error(request, "There was a problem with the payment. Please try again.")
                return redirect('checkout:error')

            # Create order marked as paid (simplified, no webhooks)
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.total_amount = total
            order.stripe_pid = intent.id
            order.status = 'paid'
            order.save()

            # clear cart
            request.session[CART_SESSION_KEY] = {}
            request.session.modified = True

            messages.success(request, 'Thanks! Your order has been received.')
            return redirect('checkout:success')
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'total': total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })


def success(request):
    return render(request, 'checkout/success.html')


def error(request):
    return render(request, 'checkout/error.html')