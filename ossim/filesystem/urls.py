from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^fileexp/(?P<choice>3)/$', views.tree),
    url(r'^fileexp/(?P<choice>2)/$', views.two),
    url(r'^fileexp/(?P<choice>1)/$', views.single),
    url(r'^fileexp/[0-9]+/process$', views.process),
    url(r'^fileexp/[0-9]+/process2$', views.process2),
]
