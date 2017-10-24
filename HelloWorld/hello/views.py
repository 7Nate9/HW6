# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import time

def index(request):
    return HttpResponse("Hello World. The time is " + time.strftime("%c") + ".")