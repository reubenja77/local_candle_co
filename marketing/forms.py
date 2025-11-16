from django import forms
from .models import NewsletterSignup, ContactRequest


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'subject', 'message']