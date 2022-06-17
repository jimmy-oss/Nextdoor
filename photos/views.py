import email
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models  import Category, Photo,Profile,FollowersCount
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from itertools import chain

def index(request):
   # user_object = User.objects.get(username=request.user.username)
    #userprofile = Profile.objects.get(user=user_object)

    return render(request, 'index.html')

def explore(request):
   # user_object = User.objects.get(username=request.user.username)
    #userprofile = Profile.objects.get(user=user_object)

    return render(request, 'explore.html')
 
 
 