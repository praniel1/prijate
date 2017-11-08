from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('register:index'))
    else:
        try :
            userprofile = UserProfile.objects.get(userim=request.user)
        except :
            userprofile = request.user
        context = {
            'userprofile' : userprofile
        # 'username' : userprofile.userim.username,
        # 'image' : userprofile.avatar
        }
        template = 'dash/index.html'
        return render(request, template, context)

def user_profile(request):
    template = 'dash/user_profile.html'
    return render(request, template)

def upload_pic(request):
    pic = request.POST['pic']
    p = UserProfile(userim=request.user, avatar=pic)
    p.save()
    return redirect('dash:index')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('register:index'))