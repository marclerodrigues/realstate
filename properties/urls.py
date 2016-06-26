from django.conf.urls import include, url

from .views import (
    properties_list,
    property_create,
)

urlpatterns = [
    url(r'^$', properties_list, name="list"),
    url(r'^create/$', property_create, name="create"),
]
