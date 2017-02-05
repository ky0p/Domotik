# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from domo.models import Group, Planning, Day, Room, Light, LightOn
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.utils.timezone import utc
import datetime
import json
import string
import re
import os

def index(request):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    context = {'now': now}
    return render(request, 'domo/index.html', context)


def planning(request):
    planning_objs = Planning.objects.order_by('id')
    day_objs = Day.objects.order_by('id')
    context = {'planning_objs': planning_objs, 'day_objs': day_objs}
    return render(request, 'domo/planning.html', context)


def rooms(request):
    rooms_obj = Room.objects.order_by('id')
    context = {'rooms_obj': rooms_obj}
    return render(request, 'domo/rooms.html', context)


def room(request, room_id):
    room_obj = get_object_or_404(Room, id=room_id)
    lights_obj = Light.objects.filter(room__exact=room_id)
    context = {'room_obj': room_obj, 'lights_obj': lights_obj}
    return render(request, 'domo/room.html', context)


def lights(request):
    lights_obj = Light.objects.order_by('id')
    context = {'lights_obj': lights_obj}
    return render(request, 'domo/lights.html', context)


def light(request, light_id):
    light_obj = get_object_or_404(Light, id=light_id)
    context = {'light_obj': light_obj}
    return render(request, 'domo/light.html', context)


def faq(request):
    return render(request, 'domo/faq.html')


# Functions

def change_state(request):

    if request.POST.get('change_state', False):
        light_id = request.POST.get('change_state').split(';')[0]
        new_state = request.POST.get('change_state').split(';')[1]

        my_changing_light = Light.objects.get(id=light_id)
	
	os.system("gpio mode " + str(my_changing_light.pin) + " out")
	os.system("gpio write " + str(my_changing_light.pin) + " 1")
	my_changing_light.state = new_state
        my_changing_light.save()

    else:

        if request.POST.get('hidden_change_state', False):
            light_id = request.POST.get('hidden_change_state').split(';')[0]
            new_state = False
	    
	    my_changing_light = Light.objects.get(id=light_id)
	    os.system("gpio mode " + str(my_changing_light.pin) + " out")
	    os.system("gpio write " + str(my_changing_light.pin) + " 0")
	    
            my_changing_light.state = new_state
            my_changing_light.save()

        else:
            messages.add_message(request, messages.ERROR,
                                 '<span class="glyphicon glyphicon-remove-sign"> </span> '
                                 'Aucune données reçues !')

    referer = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(referer)
