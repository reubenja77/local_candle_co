from decimal import Decimal

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail

import stripe

from products.models import Product
from .forms import CheckoutForm
from .models import Order


stripe.api_key = settings.STRIPE_SECRET_KEY

CART_SESSION_KEY = 'cart'


def _get_cart(request):
    """
    Always return a clean cart dict from the session.

    - Keys are product IDs as strings
    - Values are integer quantities >= 1
    """
    # Get whatever is currently in the session (or an empty dict)
    raw_cart = request.session.get(CART_SESSION_KEY, {})

    clean_cart = {}
    for pid, qty in raw_cart.items():
        try:
            qty_int = int(qty)
        except (TypeError, ValueError):
            qty_int = 1

        if qty_int > 0:
            clean_cart[str(pid)] = qty_int

    # Write the cleaned cart back to the session
    request.session[CART_SESSION_KEY] = clean_cart
    request.session.modified = True

    return clean_cart


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
    """
    Add a product to the cart, respecting quantity from the form (defaults to 1).
    """
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart = _get_cart(request)

    # Read quantity from POST, default to 1
    qty = 1
    if request.method == "POST":
        try:
            qty = int(request.POST.get("quantity", 1))
        except (TypeError, ValueError):
            qty = 1

    if qty < 1:
        qty = 1

    cart[str(product_id)] = cart.get(str(product_id), 0) + qty
    request.session.modified = True

    messages.success(request, f'Added {qty} × "{product.name}" to your cart.')
    return redirect('products:detail', slug=product.slug)


def cart_update(request, product_id):
    """
    Update the quantity of a product already in the cart.
    If quantity <= 0, remove the item.
    """
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)

    if request.method == "POST":
        try:
            qty = int(request.POST.get("quantity", 1))
        except (TypeError, ValueError):
            qty = 1

        if qty > 0:
            cart[str(product_id)] = qty
            messages.success(request, f'Updated "{product.name}" quantity to {qty}.')
        else:
            cart.pop(str(product_id), None)
            messages.info(request, f'Removed "{product.name}" from your cart.')

        request.session.modified = True

    return redirect('checkout:cart')


def cart_remove(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.pop(str(product_id), None)
    request.session.modified = True

    messages.info(request, f'Removed "{product.name}" from cart.')
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
        # No need for a flash message here; just send them back gracefully
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

            # Send a simple confirmation email (console backend in dev)
            subject = "Your Local Candle Co order"
            message = (
                f"Hi {order.full_name},\n\n"
                f"Thank you for your order from Local Candle Co.\n"
                f"Order ID: {order.id}\n"
                f"Total: R{order.total_amount}\n\n"
                "We’re getting your candles ready and will email you when they ship.\n\n"
                "Warm regards,\n"
                "Local Candle Co"
            )
            recipient_list = [order.email]

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    recipient_list,
                    fail_silently=True,  # don't break checkout if email fails
                )
            except Exception:
                # Optional: log or show a non-blocking message later
                pass

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