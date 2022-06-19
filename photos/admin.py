from django.contrib import admin
from .models import Business,Category,Profile,FollowersCount

# Register your models here.
admin.site.register(Category)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(FollowersCount)
 