from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class BlogUser(AbstractUser):
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
