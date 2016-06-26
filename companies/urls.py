from django.conf.urls import include, url
from django.contrib import admin

from .views import (
    companies_list,
    company_create,
    company_detail,
    company_update,
    company_delete,
)

urlpatterns = [
    url(r'^$', companies_list, name="list"),
    url(r'^create/$', company_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', company_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', company_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', company_delete, name="delete"),
]
