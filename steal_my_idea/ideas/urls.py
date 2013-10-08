from django.conf.urls import patterns, url

from ideas import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^ideas/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.SingleView.as_view(), name='single'),
    url(r'^page/(?P<pk>\d+)/$', views.PageView.as_view(), name='page'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<idea_id>\d+)/upvote/$', views.upvote, name='upvote'),
    url(r'^adduser/$', views.adduser, name='adduser'),
)

