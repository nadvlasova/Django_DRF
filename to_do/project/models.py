from django.db import models
from usersapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    link_to_repo = models.URLField(max_length=200)
    users_list = models.ManyToManyField(User)


class TODO(models.Model):
    name_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    field_is_active = models.BooleanField(default=True)
