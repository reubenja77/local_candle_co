from django.contrib import admin
from .models import NewsletterSignup, FAQ, ContactRequest


@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_published', 'sort_order')
    list_filter = ('is_published',)
    search_fields = ('question',)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'handled', 'created_at')
    list_filter = ('handled', 'created_at')
    search_fields = ('email', 'subject')