from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from .models import FAQ
from .forms import NewsletterForm, ContactForm, FAQForm


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks, you’re in 🌿")
            return render(request, 'marketing/newsletter_thanks.html')
    # if something’s wrong, just send back to home
    return redirect('/')


def faq_list(request):
    """Public FAQ page"""
    faqs = FAQ.objects.filter(is_published=True)
    return render(request, 'marketing/faq_list.html', {'faqs': faqs})


@staff_member_required
def faq_manage(request):
    """Admin-only FAQ management list"""
    faqs = FAQ.objects.all()
    return render(request, 'marketing/faq_manage.html', {'faqs': faqs})


@staff_member_required
def faq_create(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ created.")
            return redirect('marketing:faq_manage')
    else:
        form = FAQForm()
    return render(request, 'marketing/faq_form.html', {'form': form, 'title': 'Add FAQ'})


@staff_member_required
def faq_update(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ updated.")
            return redirect('marketing:faq_manage')
    else:
        form = FAQForm(instance=faq)
    return render(request, 'marketing/faq_form.html', {'form': form, 'title': 'Edit FAQ'})


@staff_member_required
def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        faq.delete()
        messages.success(request, "FAQ deleted.")
        return redirect('marketing:faq_manage')
    return render(request, 'marketing/faq_confirm_delete.html', {'faq': faq})


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