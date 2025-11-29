from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    path('', views.checkout_view, name='checkout'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
]
