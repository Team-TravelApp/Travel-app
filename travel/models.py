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

# class Countries(models.Model):
   # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # attractionpost = models.ForeignKey(AttractionPost,on_delete=models.CASCADE, related_name = 'comments', null=True, blank=True)



class Profile(models.Model):
    GENDER_CHOICES=(
        ('Male','Male'),
        ('Female','Female'),
        ('Non-binary', 'Non-binary')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,default='',unique=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    gender=models.CharField(max_length=100,choices=GENDER_CHOICES, null=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/profile_pics/')
    home_country = models.CharField(max_length=30,null=True,blank=True)
    followers = models.ManyToManyField(CustomUser, blank=True, related_name='followers')

    ''' followers = 
    following =
    total_countries =
    '''
    #my_countries = models.CharField(max_length=30,null=True,blank=True)
    #interest_rating = models.IntegerField
    website_url = models.URLField(max_length=255, null=True, blank=True)
    social_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user}s profile'





class AttractionPost(models.Model): 

    CONTINENTS = [
        ('EUROPE', 'EUROPE'),
        ('ASIA', 'ASIA'),
        ('AFRICA', 'AFRICA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('NORTH AMERICA', 'NORTH AMERICA'),
        ('SOUTH AMERICA', 'SOUTH AMERICA'),
        ('ANTARCTICA', 'ANTARCTICA'),
        
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country')
    continent = models.CharField(max_length=50, choices=CONTINENTS, default='NONE')
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=200, null=True)
    #TaggableManager(blank=True)
    slug = models.SlugField(null=True, unique =True)
    created_at = models.DateTimeField(auto_now_add=True)
    interest_rating = models.IntegerField(default=1,
    validators = [
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    attraction_pic = models.ImageField(upload_to="images/attractions", blank=True, null=True)

    def __str__(self):
        return self.title
        
    def star_rating(self):
        return "*"*self.interest_rating

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model): 
    comment_owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'comments')
    attraction = models.ForeignKey(AttractionPost,on_delete=models.CASCADE, related_name = 'comments', null=True, blank=True)
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

    

