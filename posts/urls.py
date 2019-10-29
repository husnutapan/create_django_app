from django.conf.urls import url

from .views import (
    post_create,
    post_detail,
    post_list,
    post_update,
    post_delete
)

urlpatterns = [
    url('create/', post_create),
    url('detail/(?P<id>\d+)/', post_detail, name="detail"),
    url('list/', post_list, name="list"),
    url('(?P<id>\d+)/edit', post_update, name="update"),
    url('(?P<id>\d+)/delete/', post_delete)
]
