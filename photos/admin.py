from django.contrib import admin
from .models import Business,Category,Neighbourhood,FollowersCount

# Register your models here.
admin.site.register(Category)
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(FollowersCount)
 