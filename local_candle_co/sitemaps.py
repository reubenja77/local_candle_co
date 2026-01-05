from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class CoreStaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            "products:list",  # your main shop/home listing view
        ]

    def location(self, item):
        return reverse(item)
