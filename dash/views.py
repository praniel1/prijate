# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request, user):
    context = {
        'username' : user,
    }
    template = 'dash/index.html'
    return render(request, template, context)