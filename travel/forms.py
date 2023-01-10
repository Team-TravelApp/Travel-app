from django import forms
from .models import Comment, CustomUser, AttractionPost, Favorite, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, EmailInput



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'bio',
            'profile_pic',
            'home_country',
            'website_url',
            'social_url', 
        ]

        widgets = {
            'bio': TextInput(attrs={
                'class': "textarea",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter a bio!'
                }),
            'website_url': TextInput(attrs={
                'class': "input", 
                'style': 'max-width: 300px;',
                'placeholder': 'Add website url'
                }),
            'social_url': TextInput(attrs={
                'class': "input", 
                'style': 'max-width: 300px;',
                'placeholder': 'Add social media url'
                })
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenttext']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class AttractionPostForm(forms.ModelForm):
    class Meta:
        model = AttractionPost
        fields = [
            'title',
            'country',
            'continent',
            'description',
            'interest_rating',
            'tags',
            'attraction_pic',
        ]

        widgets = {
            'title': TextInput(attrs={
                'class': "input",
                'style': 'max-width: 300px;',
                'placeholder': 'title'
                }),
            'description': TextInput(attrs={
                'class': "input", 
                'style': 'max-width: 300px;',
                'placeholder': 'description'
                }),
            'interest_rating': TextInput(attrs={
                'class': "input", 
                'style': 'max-width: 300px;',
                'placeholder': 'Add rating of 1-5'
                }),
            'tags': TextInput(attrs={
                'class': "input", 
                'style': 'max-width: 300px;',
                'placeholder': 'tags'
                })
        }
        
class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
           
                  
        ]        