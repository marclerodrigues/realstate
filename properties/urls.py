from django.conf.urls import include, url

from .views import (
    properties_list,
    property_create,
    property_detail,
    property_update,
    property_delete,
)

urlpatterns = [
    url(r'^$', properties_list, name="list"),
    url(r'^create/$', property_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', property_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', property_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', property_delete, name="delete"),
]
