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
    country = CountryField(blank_label='(select country)')
    description = models.TextField(blank=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    

    interest_rating = models.IntegerField(default=1,
    validators = [
        MaxValueValidator(10),
        MinValueValidator(1),
    ])

    def __str__(self):
        return self.title
        

class Comment(models.Model): 
    comment_owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'comments')
    attraction = models.ForeignKey(AttractionPost,on_delete=models.CASCADE, related_name = 'comments')
    commenttext = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.text} by:{self.comment_owner} on {self.attraction}'

    class Meta:
        ordering = ['created_at']

