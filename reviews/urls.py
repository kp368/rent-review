from django.conf.urls import patterns, url
from reviews import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^property/(?P<property_id>\d+)/$', views.property, name='property'),
    url(r'^property/(?P<property_id>\d+)/comment$', views.comment, name='comment'),
    url(r'^property/$', views.search, name='search'),
    url(r'^property/new/$', views.new, name='new'),
)
