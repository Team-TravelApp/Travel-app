from django import forms
from .models import Comment, CustomUser, AttractionPost, Favorite
from django.contrib.auth.forms import UserCreationForm, UserChangeForm





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_owner', 'attractionpost', 'commenttext')

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
            'description',
            'interest_rating',
            'tags'
            
        ]
        
class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
           
                  
        ]        