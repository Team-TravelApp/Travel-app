from django import forms
from .models import Comment, CustomUser, AttractionPost, Favorite, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'bio',
            'gender',
            'profile_pic',
            'home_country',
            'website_url',
            'social_url', 
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
            'title',
            'country',
            'continent',
            'description',
            'interest_rating',
            'tags',
            'attraction_pic',
            
        ]
        
class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
           
                  
        ]        