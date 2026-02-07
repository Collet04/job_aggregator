from django.contrib.sitemaps import Sitemap

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return []  # API-based, so empty for now
