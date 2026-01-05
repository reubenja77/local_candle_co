"""
URL configuration for local_candle_co project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from products.sitemaps import ProductSitemap
from marketing.sitemaps import MarketingStaticSitemap
from accounts.sitemaps import AccountsStaticSitemap
from local_candle_co.sitemaps import CoreStaticSitemap
from local_candle_co.views import robots_txt


sitemaps = {
    "core": CoreStaticSitemap,
    "products": ProductSitemap,
    "marketing": MarketingStaticSitemap,
    "accounts": AccountsStaticSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # allauth
    path('', include('products.urls')),
    path('checkout/', include('checkout.urls')),
    path('marketing/', include('marketing.urls')),
    path('wl/', include('accounts.urls')),
    path("robots.txt", robots_txt, name="robots_txt"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

handler404 = 'products.views.custom_404'
handler500 = 'products.views.custom_500'