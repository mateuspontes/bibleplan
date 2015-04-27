from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'sobre/?$', views.sobre),
    url(r'planos/?$', views.planos),
]