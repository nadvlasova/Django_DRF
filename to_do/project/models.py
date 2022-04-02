
from django.db import models
from usersapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    link_to_repo = models.URLField(max_length=200, blank=True)
    users_list = models.ManyToManyField(User)

    # def __str__(self):
    #     return f' {self.name} | {self.link_to_repo} | {self.users_list}'


class TODO(models.Model):
    name_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    date_create = models.DateTimeField(auto_now_add=True)

    date_update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    # def __str__(self):
    #     return f' {self.name_project} | {self.text} | {self.date_create} | {self.date_update} | {self.creator} | {self.is_active}'

    # date_create = date_create.strftime("%m/%d/%Y, %h:%m:%s")
