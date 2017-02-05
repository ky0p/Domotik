#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ky0p'

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'autodl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^domo/', include('domo.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
