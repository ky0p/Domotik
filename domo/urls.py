# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from domo import views

urlpatterns = [
                       url(r'^$', views.index, name='index'),
                       url(r'^planning/$', views.planning, name='planning'),
                       url(r'^rooms/$', views.rooms, name='rooms'),
                       url(r'^lights/$', views.lights, name='lights'),
                       url(r'^rooms/(?P<room_id>\d+)/$', views.room, name='room'),
                       url(r'^lights/(?P<light_id>\d+)/$', views.light, name='light'),
                       url(r'^change_state/$', views.change_state, name='change_stage'),
                       url(r'^faq/$', views.faq, name='faq'),
                       ]
