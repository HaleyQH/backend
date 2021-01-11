from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from polls import views

from polls.views import UserViewSet

urlpatterns = [
    url(r'^', UserViewSet.as_view()),
    url(r'^(?P<pk>\d+)/$', UserViewSet.as_view({'get': 'retrieve'})),
    # url(r'^/query', UserViewSet.as_view({'post': 'query'})),

    #     ,'post':'retrieve' {'get':'retrieve'}
]
