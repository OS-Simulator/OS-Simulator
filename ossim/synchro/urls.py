from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'synchro'
urlpatterns =[
    url(r'^semaphores/$', views.semaphores, name='semaphores'),
    url(r'^socket/$', views.socket, name='socket'),
    url(r'^deadlocks/$', views.deadlocks, name='deadlocks'),
    url(r'^semaphores/demo/(?P<pk>[0-9]+)/$', views.sem_demo, name='sem_demo'),
    url(r'^socket/demo/(?P<pk>[0-9]+)/$', views.socket_demo, name='socket_demo'),
    url(r'^bankalgo/$', views.bankalgo, name='bankalgo'),
]
