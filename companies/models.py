from __future__ import unicode_literals

from django.db import models

from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    domain = models.CharField(max_length=240)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("companies:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug

    query_search = Company.objects.filter(slug=slug).order_by("-id")

    if query_search.exists():
        new_slug = "%s-%s" %(slug, query_search.first().id)
        return create_slug(instance, new_slug=new_slug)

    return slug

def pre_save_company_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_company_receiver, sender=Company)
