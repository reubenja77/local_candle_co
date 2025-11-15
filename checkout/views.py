from django.shortcuts import render
from django.http import HttpResponse

def checkout_view(request):
    return HttpResponse("Checkout page placeholder for Local Candle Co.")

def cart_add(request, product_id):
    """Add a product to the cart (stored in session)."""
    product = get_object_or_404(Product, id=product_id)

    # Get current cart from session or start with empty
    cart = request.session.get('cart', {})

    # Use string keys because session data is JSON-serializable
    product_key = str(product_id)
    cart[product_key] = cart.get(product_key, 0) + 1

    # Save back to session
    request.session['cart'] = cart

    # For now, redirect to a simple cart detail page
    return redirect('checkout:cart_detail')


def cart_detail(request):
    """Show what's currently in the cart."""
    cart = request.session.get('cart', {})

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    items = []
    total = 0

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