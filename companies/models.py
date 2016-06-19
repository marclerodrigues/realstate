from __future__ import unicode_literals

from django.db import models

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

    class Meta:
        ordering = ["-timestamp"]
