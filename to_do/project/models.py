from django.db import models
from django.db.models import Prefetch

from usersapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    link_to_repo = models.URLField(max_length=200, blank=True)
    users_list = models.ManyToManyField(User)


class TODO(models.Model):
    name_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True, blank=True)

    date_update = models.DateTimeField(auto_now=True, blank=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, blank=True)



    # def __str__(self):
    #     return str(self.name_project)
