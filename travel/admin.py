from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AttractionPost, Comment, Following, Favorite, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(AttractionPost)
admin.site.register(Comment)
admin.site.register(Following)
admin.site.register(Favorite)