from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.index,name='index'),
    path('explore',views.explore,name='explore'),
    path('business/<str:pk>/',views.viewBusiness, name='business'),
    path('add',views.addBusiness, name='add'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('settings',views.settings, name='settings'),
    path('neighbourhood/<str:pk>',views.neighbourhood, name='neighbourhood'),
    path('logout',views.logout, name='logout'),
  
]