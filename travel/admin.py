from django.contrib import admin
from .models import User, Attraction, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Attraction)
admin.site.register(Comment)