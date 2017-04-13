from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'synchro'
urlpatterns =[
    url(r'^$', views.home, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^demo/(?P<pk>[0-9]+)/$', views.demo, name='demo'),

]
