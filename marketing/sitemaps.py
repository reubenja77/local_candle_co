from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class MarketingStaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return [
            "marketing:faq",
            "marketing:contact",
        ]

    def location(self, item):
        return reverse(item)
