import graphene
from graphene_django import DjangoObjectType

from project.models import Project
from usersapp.models import User


class Query(graphene.ObjectType):
    hello = graphene.String(default_value='hi')


schema = graphene.Schema(query=Query)


# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'


# class Query(graphene.ObjectType):
#     all_users = graphene.List(UserType)
#
#     def resolve_all_users(root, info):
#         return User.objects.all()
#
#
# schema = graphene.Schema(query=Query)
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
