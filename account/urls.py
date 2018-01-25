#coding:utf8
__author__ = 'Li'

from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^checkname/$', views.checkname, name='checkname'),
]