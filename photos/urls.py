from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.index,name='index'),
    path('explore',views.explore,name='explore'),
    #path('photo/<str:pk>/',views.viewPhoto, name='photo'),
    #path('add',views.addPhoto, name='add'),
   # path('search', views.search, name='search'),
  #  path('profile/<str:pk>',views.profile, name='profile'),
  #  path('settings',views.settings, name='settings'),
  #  path('signup',views.signup, name='signup'),
  #  path('signin',views.signin, name='signin'),
  #  path('logout',views.logout, name='logout'),
]