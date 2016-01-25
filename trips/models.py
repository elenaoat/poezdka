from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('Publishing date', default=timezone.now)
    image = models.ImageField()
    image_post = models.ImageField()
    image_description = models.CharField(max_length=200, default="")
    teaser = models.TextField()
    text = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
    	if not self.id:
    		self.slug = slugify(self.title)
    	super(Post, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('view_post', kwargs={'post_slug': self.slug})

