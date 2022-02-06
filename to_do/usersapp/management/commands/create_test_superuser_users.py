from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from usersapp.models import User


class Command(BaseCommand):
    help = 'Create random usersapp'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Количество создаваемых пользователей')
        # parser.add_argument('-p', '--prefix', type=str, help='Префикс для username')
        # parser.add_argument('-a', '--admin', action='store_true', help='Создание учетной записи администратора')

    def handle(self, *args, **kwargs):
        # def handle(self, *args, **options):
        User.objects.all().delete()
        user_total = kwargs['total']
        # prefix = kwargs['prefix']
        # admin = kwargs['admin']
        User.objects.create_superuser('nadezhda', 'nadezhda@mail.com', '123')

        for i in range(user_total):
            User.objects.create_user(f'user{i}', f'user{i}@test.com', '123')
        print('done')

        # if prefix:
        #     username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
        # else:
        #     username = get_random_string()
        #
        # if admin:
        #     User.objects.create_superuser(username=username, email='', password='123')
        # else:
        #     User.objects.create_user(username=username, email='', password='12345')
