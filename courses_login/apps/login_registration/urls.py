from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process, name='process'),
    url(r'^success$', views.success, name='success'),
    url(r'^login$', views.login),
    url(r'^logoff$', views.clear)
]
