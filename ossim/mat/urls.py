from django.conf.urls import url
from mat import views

app_name = 'mat'

urlpatterns = [
    url(r'^$',views.home_page, name="home"),
    url(r'^mft/$', views.mat_mft_get_data, name="mat-get-data"),
    url(r'^mvt/$', views.mat_mvt_get_data, name="mvt-get-data"),
]
