from django.core.management.base import BaseCommand

from usersapp.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create(first_name='test', last_name='test', email='test@mail.ru')