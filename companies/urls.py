from django.conf.urls import include, url
from django.contrib import admin

from .views import (
    companies_list,
    company_create,
    company_detail,
)

urlpatterns = [
    url(r'^$', companies_list, name="list"),
    url(r'^create/$', company_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', company_detail, name="detail"),
]
