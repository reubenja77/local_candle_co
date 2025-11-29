from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import WishlistItem


@login_required
def wishlist(request):
    items = WishlistItem.objects.filter(user=request.user).select_related('product')
    return render(request, 'accounts/wishlist.html', {'items': items})


@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    messages.success(request, 'Added to wishlist.')
    return redirect('products:detail', slug=product.slug)


@login_required
def wishlist_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    messages.info(request, 'Removed from wishlist.')
    return redirect('accounts:wishlist')
