from django.conf.urls import include, url
from django.contrib import admin

from .views import (
    companies_list,
)

urlpatterns = [
    url(r'^$', companies_list, name="list"),
]
