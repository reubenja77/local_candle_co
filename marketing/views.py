from django.shortcuts import render, redirect
from django.contrib import messages

from .models import FAQ
from .forms import NewsletterForm, ContactForm


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks, you’re in 🌿")
            return render(request, 'marketing/newsletter_thanks.html')
    # if something’s wrong, send back to home
    return redirect('/')


def faq_list(request):
    faqs = FAQ.objects.filter(is_published=True)
    return render(request, 'marketing/faq_list.html', {'faqs': faqs})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! We’ll get back to you shortly.")
            return render(request, 'marketing/contact_thanks.html')
    else:
        form = ContactForm()
    return render(request, 'marketing/contact.html', {'form': form})