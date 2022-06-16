from django.contrib import admin
from .models import Photo,Category,Profile,FollowersCount

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Profile)
admin.site.register(FollowersCount)
 