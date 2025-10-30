from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):

    #Linking to Django User model -> 1 User = 1 member
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    dob = models.DateField(null=True, blank=True) #optional
    size = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    bf = models.FloatField(null=True, blank=True)
    lift = models.BooleanField(default=False)
    run = models.BooleanField(default=False)
    

    
    def __str__(self):
        return f"{self.user.username}" #Username from User model

