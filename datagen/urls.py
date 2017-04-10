from django.conf.urls import url
from . import views, search

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', search.search_post),
    url(r'^manual$', views.manual, name='User Manual'),
    url(r'^documentation$', views.documentation, name='Documentation'),
]
