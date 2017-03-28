from django.conf.urls import url
from feirapp import views

urlpatterns = [
    url(r'feira/$',views.FeiraCreateList.as_view()),
    url(r'feira/update/(?P<pk>\d+)/$',views.FeiraUpdate.as_view()),
    url(r'feira/delete/(?P<pk>\d+)/$',views.FeiraDestroy.as_view()),
]
