import email
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models  import Category, Business,Neighbourhood,FollowersCount
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from itertools import chain
import random

@login_required(login_url='signin')
def index(request):
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

                #create a Neighbourhood object for the new user
                user_model = User.objects.get(username=username)
                new_neighbourhood = Neighbourhood.objects.create(user=user_model, id_user=user_model.id)
                new_neighbourhood.save()
                return redirect('index')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')   
     
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def settings(request):
    user_neighbourhood = Neighbourhood.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_neighbourhood.profileimg
            bio = request.POST['bio']
            email_address = request.POST['email_address']
            phone_number = request.POST['phone_number']
            location = request.POST['location']
            neighbour_name = request.POST['neighbour_name']

            user_neighbourhood.profileimg = image
            user_neighbourhood.bio = bio
            user_neighbourhood.location = location
            user_neighbourhood.email_address = email_address
            user_neighbourhood.neighbour_name = neighbour_name
            user_neighbourhood.phone_number = phone_number
            user_neighbourhood.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            email_address = request.POST['email_address']
            phone_number = request.POST['phone_number']
            location = request.POST['location']
            neighbour_name = request.POST['neighbour_name']

            user_neighbourhood.profileimg = image
            user_neighbourhood.bio = bio
            user_neighbourhood.location = location
            user_neighbourhood.email_address = email_address
            user_neighbourhood.phone_number = phone_number
            user_neighbourhood.neighbour_name = neighbour_name
            user_neighbourhood.save()
        
        return redirect('settings')
    return render(request, 'setting.html', {'user_neighbourhood': user_neighbourhood})

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/neighbourhood/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/neighbourhood/'+user)
    else:
        return redirect('/')

@login_required(login_url='signin')
def explore(request):
       user_object = User.objects.get(username=request.user.username)
       user_neighbourhood = Neighbourhood.objects.get(user=user_object)
       
       user_following_list = []  
       user_following = FollowersCount.objects.filter(follower=request.user.username)
       
       for users in user_following:  
        user_following_list.append(users.user)  
        
       category = request.GET.get('category')
       if category == None:
            businesses = Business.objects.all()
       else:
           businesses = Business.objects.filter(category__name = category)
           
       category = Category.objects.all()
       context = {'categories':category,'businesses':businesses,'user_neighbourhood': user_neighbourhood,}

       return render(request, 'explore.html', context)
      
      

@login_required(login_url='signin')
def viewBusiness (request, pk):
       business = Business.objects.get(id=pk)
       return render(request,'business.html',{'business':business})   
    
@login_required(login_url='signin')
def addBusiness (request):
       category = Category.objects.all()
       if request.method == 'POST':
        user = request.user.username
        data = request.POST
        image = request.FILES.get('image')
       
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                 
                name=data['category_new'])
        else:
            category = None
            
        business = Business.objects.create(
                category=category,
                 user=user,
                description=data['description'],
                image=image,
                email_address=data['email_address'],
            )
         

        return redirect('explore') 
       context = {'categories': category}
       return render(request, 'add.html', context) 

@login_required(login_url='signin')
def neighbourhood(request, pk):
    user_object = User.objects.get(username=pk)
    user_neighbourhood = Neighbourhood.objects.get(user=user_object)
    user_posts = Business.objects.filter(user=pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))
    

    context = {
        'user_object': user_object,
        'user_neighbourhood': user_neighbourhood,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
        
    }
    return render(request, 'neighbourhood.html', context)

@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_neighbourhood = Neighbourhood.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_neighbourhood = []
        username_neighbourhood_list = []

        for users in username_object:
            username_neighbourhood.append(users.id)

        for ids in username_neighbourhood:
            neighbourhood_lists = Neighbourhood.objects.filter(id_user=ids)
            username_neighbourhood_list.append(neighbourhood_lists)
        
        username_neighbourhood_list = list(chain(*username_neighbourhood_list))
    return render(request, 'search.html', {'user_neighbourhood': user_neighbourhood, 'username_neighbourhood_list': username_neighbourhood_list})
 
 

 
 