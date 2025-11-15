from django.http import HttpResponse

def wishlist_add(request, product_id):
    return HttpResponse(f"Wishlist placeholder – would add product {product_id} for user {request.user}.")