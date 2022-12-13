from django import forms
from .models import Comment, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_owner', 'attraction', 'commenttext')

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")
