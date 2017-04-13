from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'memory'
urlpatterns =[
    url(r'^page/$', views.page, name='page'),
    url(r'^alloc/$', views.alloc, name='alloc'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^fifo/$', views.fifo, name='fifogateway'),
]
