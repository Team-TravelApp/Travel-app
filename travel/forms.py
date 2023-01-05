from django import forms
from .models import Comment, CustomUser, AttractionPost, Favorite, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'user',
            'bio',
            'profile_pic',
            'website_url',
            'facebook_url', 
            'twitter_url',
            'instagram_url',
            'home_country',
        ]



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_owner', 'commenttext')

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
            'user',
            'title',
            'country',
            'continent',
            'description',
            'interest_rating',
            'tags',
            
        ]
        
class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
           
                  
        ]        