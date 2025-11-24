from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('newsletter/', views.newsletter_signup, name='newsletter'),

    # Public FAQ page
    path('faq/', views.faq_list, name='faq'),

    # Admin FAQ CRUD
    path('faq/manage/', views.faq_manage, name='faq_manage'),
    path('faq/add/', views.faq_create, name='faq_add'),
    path('faq/<int:pk>/edit/', views.faq_update, name='faq_edit'),
    path('faq/<int:pk>/delete/', views.faq_delete, name='faq_delete'),

    path('contact/', views.contact, name='contact'),
]