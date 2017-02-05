# -*- coding: utf-8 -*-
from django.contrib import admin
from domo.models import Group, Planning, Room, LightOn, Day, Light

admin.site.register(Group)
admin.site.register(Planning)
admin.site.register(Room)
admin.site.register(LightOn)
admin.site.register(Day)
admin.site.register(Light)