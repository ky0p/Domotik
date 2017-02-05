# -*- coding: utf-8 -*-
from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Planning(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    picture = models.ImageField(upload_to='static/domo', null=True)
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return u'{}'.format(self.name)


class Day(models.Model):
    name = models.CharField(max_length=10)
    planning = models.ForeignKey('Planning')

    def __unicode__(self):
        return u'{}'.format(self.name)


class LightOn(models.Model):
    id = models.AutoField(primary_key=True)
    planning = models.ForeignKey('Planning')
    day = models.ForeignKey('Day')
    duration = models.IntegerField(default=0, null=True)
    light_on_start = models.TimeField(null=True)

    def __unicode__(self):
        return u'{}'.format(self.id)


class Light(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    pin = models.PositiveIntegerField()
    state = models.BooleanField(default=False)
    room = models.ForeignKey('Room', null=True)
    light_on_start = models.ForeignKey('LightOn', blank=True, null=True)

    def __unicode__(self):
        return u'{}'.format(self.name)
