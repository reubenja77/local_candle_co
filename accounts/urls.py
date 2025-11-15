from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('wishlist/add/<int:product_id>/', views.wishlist_add, name='wishlist_add'),
]