from decimal import Decimal

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail

import stripe

from products.models import Product
from .forms import CheckoutForm

stripe.api_key = settings.STRIPE_SECRET_KEY

CART_SESSION_KEY = "cart"


def _get_cart(request):
    """
    Return the cart dictionary from the session.

    Keys are product IDs (as strings), values are quantities (ints).
    """
    cart = request.session.setdefault(CART_SESSION_KEY, {})
    for pid, qty in list(cart.items()):
        try:
            cart[pid] = int(qty)
        except (TypeError, ValueError):
            cart[pid] = 1
    return cart


def cart_view(request):
    cart = _get_cart(request)
    items = []
    total = Decimal("0.00")

    for pid, qty in cart.items():
        product = get_object_or_404(Product, id=int(pid), is_active=True)
        line_total = Decimal(qty) * product.price
        items.append(
            {
                "product": product,
                "qty": qty,
                "line_total": line_total,
            }
        )
        total += line_total

    return render(
        request,
        "checkout/cart.html",
        {"items": items, "total": total},
    )


def cart_add(request, product_id):
    """
    Add product to cart, respecting quantity from the form (defaults to 1).
    """
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart = _get_cart(request)

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

    messages.success(
        request,
        f'Added {qty} × "{product.name}" to your cart.',
    )
    return redirect("products:detail", slug=product.slug)


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
            messages.success(
                request,
                f'Updated "{product.name}" quantity to {qty}.',
            )
        else:
            cart.pop(str(product_id), None)
            messages.info(
                request,
                f'Removed "{product.name}" from your cart.',
            )

        request.session.modified = True

    return redirect("checkout:cart")


def cart_remove(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.pop(str(product_id), None)
    request.session.modified = True

    messages.info(
        request,
        f'Removed "{product.name}" from cart.',
    )
    return redirect("checkout:cart")


def _calculate_cart_total(request):
    """
    Helper to calculate total from cart.
    """
    cart = _get_cart(request)
    total = Decimal("0.00")
    for pid, qty in cart.items():
        product = get_object_or_404(Product, id=int(pid), is_active=True)
        total += Decimal(qty) * product.price
    return total


def checkout_view(request):
    """
    Checkout with Stripe Elements.

    - GET: show checkout form + card input,
      create PaymentIntent and send client_secret.
    - POST: Stripe JS confirms PaymentIntent,
      then we create an Order, clear cart, send email.
    """
    cart = _get_cart(request)
    if not cart:
        messages.info(request, "Your cart is empty.")
        return redirect("products:list")

    total = _calculate_cart_total(request)

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            stripe_pid = request.POST.get("stripe_pid", "")

            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.total_amount = total
            order.stripe_pid = stripe_pid
            order.status = "paid"
            order.save()

            # Send a simple confirmation email (console backend in dev)
            subject = "Your Local Candle Co order"
            message = (
                f"Hi {order.full_name},\n\n"
                "Thank you for your order from Local Candle Co.\n"
                f"Order ID: {order.id}\n"
                f"Total: R{order.total_amount}\n\n"
                "We’re getting your candles ready and will email you "
                "when they ship.\n\n"
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
                    fail_silently=True,
                )
            except Exception:
                # In production you would log this instead of pass
                pass

            # Clear cart
            request.session[CART_SESSION_KEY] = {}
            request.session.modified = True

            success_msg = (
                "Thanks! Your payment was successful and your "
                "order has been received."
            )
            messages.success(request, success_msg)
            return redirect("checkout:success")
    else:
        form = CheckoutForm()

    # For GET and invalid POST, (re)create a PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount=int(total * 100),  # cents
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        "form": form,
        "total": total,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }
    return render(request, "checkout/checkout.html", context)


def success(request):
    return render(request, "checkout/success.html")


def error(request):
    return render(request, "checkout/error.html")
