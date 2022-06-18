import email
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models  import Category, Photo,Profile,FollowersCount
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from itertools import chain

def index(request):
    #user_object = User.objects.get(username=request.user.username)
    #userprofile = Profile.objects.get(user=user_object)

    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
               

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')

def explore (request):
       category = request.GET.get('category')
       if category == None:
            photos = Photo.objects.all()
       else:
           photos = Photo.objects.filter(category__name = category)
           
       category = Category.objects.all()
       context = {'categories':category,'photos':photos}

       return render(request, 'explore.html', context)
 
 

 
 