from django.conf.urls import patterns, url

from micro import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<account_id>\d+)/$', views.detail, name='detail'))