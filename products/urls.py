from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('', views.product_list, name='list'),
    path('p/<slug:slug>/', views.product_detail, name='detail'),
    path('error-test/', views.test_error, name='error_test'),
]
