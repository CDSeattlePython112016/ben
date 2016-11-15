from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^confirm/(?P<id>\d+)$', views.confirm, name='confirm'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^add_user_to_course$', views.users_courses, name='add_page'),
    url(r'^add_user$', views.add_user, name='add_user'),
]
