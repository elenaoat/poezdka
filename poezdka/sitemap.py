from django.contrib.sitemaps import Sitemap
from trips.models import Post

class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date