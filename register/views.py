# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    if not request.user.is_authenticated():
        template = 'register/index.html'
        return render(request, template)
    else:
        return HttpResponseRedirect(reverse('dash:index'))

def contact(request):
    if not request.user.is_authenticated():
        template = 'register/contact.html'
        return render(request, template)
    else:
        return HttpResponseRedirect(reverse('dash:index'))

def index2(request):
    if not request.user.is_authenticated():
        template = 'register/index2.html'
        return render(request, template)
    else:
        return HttpResponseRedirect(reverse('dash:index'))

def index3(request):
    if not request.user.is_authenticated():
        template = 'register/index3.html'
        return render(request, template)
    else:
        return HttpResponseRedirect(reverse('dash:index'))

def client_register(request):
    if not request.user.is_authenticated():
        user = request.POST['usernamesignup']
        mail = request.POST['emailsignup']
        password = request.POST['passwordsignup']
        users = User.objects.create_user(username=user,email=mail, password=password)
        users.save()
        login(request,user)
        return HttpResponseRedirect(reverse('dash:index'))
    else:
        return HttpResponseRedirect(reverse('dash:index'))

def client_login(request):
    user = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=user, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('dash:index'))
    else:
        return HttpResponse("Invalid credentials")

def org_register(request):
    if not request.user.is_authenticated():
        username = request.POST['user_name']
        mail = request.POST['mail']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=mail, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('dash:index'))
    else:
        return HttpResponseRedirect(reverse('dash:index'))

def org_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('dash:index'))
    else:
        return HttpResponse("Invalid credentials")