from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    # email = models.EmailField(verbose_name="Email", max_length=250, unique=True)
    email = models.EmailField(unique=True)


class Project(models.Model):
    name = models.CharField(max_length=64)
    link_to_repo = models.query_utils
    users_list = models.ManyToManyField(User)


class TODO(models.Model):
    name_project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField
