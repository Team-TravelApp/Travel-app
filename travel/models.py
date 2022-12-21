from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager


# Create your models here.
class CustomUser(AbstractUser):
    pass


def __str__(self):
    return self.username


class AttractionPost(models.Model): 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    country = models.TextField(blank=True)
    description = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    interest_rating = models.IntegerField(default=1,
    validators = [
        MaxValueValidator(10),
        MinValueValidator(1),
    ])
    image = models.ImageField(upload_to='postimage', blank=True, null=True)

    def __str__(self):
        return self.title
        
    def star_rating(self):
        return "*"*self.interest_rating

class Comment(models.Model): 
    comment_owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'comments')
    attractionpost = models.ForeignKey(AttractionPost,on_delete=models.CASCADE, related_name = 'comments', null=True, blank=True)
    commenttext = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'favorites')
    attraction = models.ForeignKey(AttractionPost, on_delete=models.CASCADE, related_name ='favorites')    

    def __str__(self):
        return self.attraction.title

class Following(models.Model):
    current_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='curent_users')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follow')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['current_user', 'following'], name='follower_relationship')
        ]

    def __str__(self):
        return f"{self.current_user} is following {self.following}"

    

