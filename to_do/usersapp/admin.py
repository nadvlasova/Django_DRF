from django.contrib import admin

from django.contrib import admin
from usersapp.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)

# from .models import User

# admin.site.register(User)
