from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.



class NewProfileModel(models.Model):
    profileURL = models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=200, default="")
    password2 = models.CharField(max_length=200, default="")
    foreignkeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

def __str__(self):
    return "This recipe creator is: " + str(self.name)


class RecipeModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    imageURL = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=1000, blank=True, null=True)
    directions = models.TextField(max_length=10, blank=True, null=True)
    dateCreated= models.DateField(default=timezone.now)
    foreignkeyToNewProfile = models.ForeignKey(NewProfileModel, on_delete=models.CASCADE, blank=True, null=True)

def __str__(self):
    return "This Recipe is called: " + str(self.name)



