from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Attraction, Comment
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Attraction)
admin.site.register(Comment)