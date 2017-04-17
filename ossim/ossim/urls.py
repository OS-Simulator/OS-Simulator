"""ossim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^job/', include('job.urls')),
    url(r'^disk/', include('disk.urls')),
    url(r'^synchro/', include('synchro.urls')),
    url(r'^process/', include('process.urls')),
    url(r'^memory/', include('memory.urls')),
    url(r'^matdemo/', include('mat.urls')),
    url(r'^mat/', views.matindex),
    url(r'^filesystem/', include('filesystem.urls')),
    url(r'^wiki/', include('wikipages.urls')),
]
