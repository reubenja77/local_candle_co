from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('newsletter/', views.newsletter_signup, name='newsletter'),
    path('faq/', views.faq_list, name='faq'),
    path('contact/', views.contact, name='contact'),
]