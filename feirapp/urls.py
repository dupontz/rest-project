from django.conf.urls import url
from django.contrib import admin
from feirapp import views
urlpatterns = [
    url(r'^feira/$', views.feira_list),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
