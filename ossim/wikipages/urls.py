from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bankers/$', views.bankers),
    url(r'^disk/$', views.disk),
    url(r'^semaphore/$', views.semaphore),
    url(r'^mem/$', views.mem),
    url(r'^pra/$', views.pra),
    url(r'^process/$', views.process),
    url(r'^socket/$', views.socket),
]
