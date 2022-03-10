import json
import math

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
# from django.contrib.auth.models import User

from usersapp.views import UserModelViewSet
from usersapp.models import User
from project.models import Project, TODO


class TestUserModelViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin@admin.com'
        self.admin = User.objects.create_superuser(self.name, self.email, self.password)

        self.data = {'username': 'ivan', 'first_name': 'Ivan', 'last_name': 'Petrov', 'email': 'ivan@mail.com'}
        self.data_put = {'username': 'ivan', 'first_name': 'IVAN', 'last_name': 'PETROV', 'email': 'IVAN@mail.com'}
        self.url = '/api/usersapp/'

    # APIRequestFactory force_authenticate
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request, self.admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #         # APIClient

    def test_get_detail(self):
        client = APIClient()
        user = User.objects.create(**self.data)  # создаем юзера
        response = client.get(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_guest(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        response = client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_admin(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_ = User.objects.get(id=user.id)
        self.assertEqual(user_.first_name, self.data_put.get('first_name'))
        self.assertEqual(user_.last_name, self.data_put.get('last_name'))
        self.assertEqual(user_.email, self.data_put.get('email'))

        client.logout()

    def tearDown(self) -> None:
        pass


#     # APISimpleTestCase


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)


#     # APITestCase


class TestProject(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin@admin.com'

        self.data = {'username': 'ivan', 'first_name': 'Иван', 'last_name': 'Петров', 'email': 'ivan@ivan.com'}
        self.data_put = {'username': 'ivan', 'first_name': 'IVAN', 'last_name': 'PETROV', 'email': 'IVAN@mail.com'}
        self.url = '/api/projects/'
        self.admin = User.objects.create_superuser(self.name, self.email, self.password)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_admin(self):
        user = User.objects.create(**self.data)
        project_1 = Project.objects.create(name='NAME', link_to_repo='https://www.yahoo.com')
        # todo1 = TODO.objects.create(name_project='name', creator=user)  # уточнить создателя

        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project_1.id}/', {'name': 'NewTestProject',
                                                                  'link_to_repo': 'https://www.yahoo.com'})
        # response = self.client.put(f'{self.url}{todo1.id}/', {'name_project': 'NewTodo', 'creator': todo1.creator.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_2 = Project.objects.get(id=project_1.id)
        # todo2 = TODO.objects.get(id=todo1.id)
        self.assertEqual(project_2.name, 'NewTestProject')
        # self.assertEqual(todo2.name_project, 'NewTodo')
        self.client.logout()

    def test_put_mixer(self):
        project_3 = mixer.blend(TODO)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project_3.id}/', {'name': 'NewTestProject_3',
                                                                  'link_to_repo': 'https://www.yahoo.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_4 = Project.objects.get(id=project_3.id)
        self.assertEqual(project_4.name, 'NewTestProject_3')
        self.client.logout()

    def test_put_mixer_fields(self):
        project_5 = mixer.blend(TODO, name='NewTestProject_4')
        self.assertEqual(project_5.name, 'NewTestProject_4')
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project_5.id}/', {'name': 'NewTestProject_4', 'link_to_repo': 'https://www.yahoo.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_6 = Project.objects.get(id=project_5.id)
        self.assertEqual(project_6.name, 'NewTestProject_4')
        self.client.logout()
