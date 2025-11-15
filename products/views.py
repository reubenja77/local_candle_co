from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm

def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    form = None
    if request.user.is_authenticated:
        instance = Review.objects.filter(product=product, author=request.user).first()
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=instance)
            if form.is_valid():
                r = form.save(commit=False)
                r.product = product
                r.author = request.user
                r.save()
                messages.success(request, 'Review saved.')
                return redirect('products:detail', slug=slug)
        else:
            form = ReviewForm(instance=instance)
    reviews = product.reviews.all()
    return render(request, 'products/detail.html', {'product': product, 'reviews': reviews, 'form': form})

def custom_404(request, exception): return render(request, '404.html', status=404)
def custom_500(request): return render(request, '500.html', status=500)