from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name="Email", max_length=250, unique=True)
