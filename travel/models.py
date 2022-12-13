from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    pass

class AttractionPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    title = models.CharField(max_length=200),
    country = models.CountryField(blank_label='(select country'),
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    interest_rating = models.IntegerField(default=1,
    validators = [
        MaxValueValidator(10),
        MinValueValidator(1),
    ]
)
    def __str__(self):
        return self.title
