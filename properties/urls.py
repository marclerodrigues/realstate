from django.conf.urls import include, url

from .views import (
    properties_list,
)

urlpatterns = [
    url(r'^$', properties_list, name="list"),
]
