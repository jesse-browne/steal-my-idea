from django.conf.urls import patterns, url

from ideas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<idea_id>\d+)/$', views.single, name='single'),
    url(r'^(?P<idea_id>\d+)/upvote/$', views.upvote, name='upvote'),
    url(r'^(?P<idea_id>\d+)/results/$', views.results, name='results'),
)