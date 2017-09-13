# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    template = 'register/index.html'
    return render(request, template)

def contact(request):
    template = 'register/contact.html'
    return render(request, template)

def index3(request):
    template = 'register/index3.html'
    return render(request, template)

def client_register(request):
    user = request.POST['usernamesignup']
    mail = request.POST['emailsignup']
    password = request.POST['passwordsignup']
    users = User.objects.create_user(username=user,email=mail, password=password)
    users.save()
    return HttpResponseRedirect(reverse('dash:index', args=[user,]))

