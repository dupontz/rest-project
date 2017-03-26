from django.conf.urls import url
from rest_framework import generics
from django.contrib import admin
from models import Feira

from feirapp.serializers import FeiraSerializer
from feirapp import views
urlpatterns = [
    url(r'feira/$',views.FeiraList.as_view()),
]
