from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/<int:product_id>/', views.wishlist_add, name='wishlist_add'),
    path('remove/<int:product_id>/', views.wishlist_remove, name='wishlist_remove'),
]
