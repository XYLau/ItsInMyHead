from django.conf.urls import url
from . import views, search

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search-post$', search.search_post),
]
