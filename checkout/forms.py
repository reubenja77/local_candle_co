from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'address_line1',
            'address_line2',
            'city',
            'postal_code',
            'country',
        ]
