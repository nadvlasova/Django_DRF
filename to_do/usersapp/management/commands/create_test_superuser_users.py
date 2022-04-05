from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from usersapp.models import User


class Command(BaseCommand):
    help = 'Create random usersapp'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        # def handle(self, *args, **options):
        User.objects.all().delete()
        user_total = kwargs['total']

        User.objects.create_superuser('nadezhda', 'nadezhda@mail.com', '1',
                                      first_name='Nadezhda',
                                      last_name='Vlasova')

        for i in range(user_total):
            User.objects.create_user(f'user{i}', f'user{i}@test.com', '123',
                                     first_name=(f'user{i} FirstName'),
                                     last_name=(f'user{i} LastName'))

        print('done')
