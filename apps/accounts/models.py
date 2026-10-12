from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=50,unique=True)
    bio=models.TextField()
    avatar=models.ImageField(upload_to='images/')

    # USERNAME_FIELD = 'phone_number'  
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
