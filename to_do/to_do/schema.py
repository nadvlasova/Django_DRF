import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from project.models import Project, TODO
from usersapp.models import User


# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value='hi')
#
#
# schema = graphene.Schema(query=Query)

# --------------
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class Query(graphene.ObjectType):
#     all_users = graphene.List(UserType)
#
#     def resolve_all_users(root, info):
#         return User.objects.all()
#
#
# schema = graphene.Schema(query=Query)
# ----------------

# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class Query(graphene.ObjectType):
#     all_users = graphene.List(UserType)
#     projects = graphene.List(ProjectType)
#
#     def resolve_all_users(root, info):
#         return User.objects.all()
#
#     def resolve_all_projects(root, info):
#         return Project.objects.all()
#
#
# schema = graphene.Schema(query=Query)

# ---------------

# class TODOType(DjangoObjectType):
#     class Meta:
#         model = TODO
#         fields = '__all__'
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class Query(ObjectType):
#
#     users = graphene.List(UserType)
#     projects = graphene.List(ProjectType)
#     todos = graphene.List(TODOType)
#
#     def resolve_users(root, info):
#         return User.objects.all()
#
#     def resolve_projects(root, info):
#         return Project.objects.all()
#
#     def resolve_todos(root, info):
#         return TODO.objects.all()
#
#
# schema = graphene.Schema(query=Query)
#
# --------------
# фильтрация по id
# class TODOType(DjangoObjectType):
#     class Meta:
#         model = TODO
#         fields = '__all__'
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class Query(ObjectType):
#     user_id = graphene.Field(UserType, id=graphene.Int())
#
#     def resolve_user_id(root, info, id=None):
#         try:
#             return User.objects.get(id=id)
#         except User.DoesNotExist:
#             return None
#
#     # фильтрация по связанному полю
#     todos_by_creator = graphene.List(TODOType, username=graphene.String(required=False))
#     def resolve_todos_by_creator(root, info, username=None):
#         todos = TODO.objects.all()
#         if username:
#             todos = todos.filter(creator__username=username)
#         return todos
#
# schema = graphene.Schema(query=Query)

# * обработать запрос в случае если нет  id вывести весь список

# --------------

# мутации

class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(ObjectType):
    user_id = graphene.Field(UserType, id=graphene.Int())

    def resolve_user_id(root, info, id=None):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    todos_by_creator = graphene.List(TODOType, username=graphene.String(required=False))

    def resolve_todos_by_creator(root, info, username=None):
        todos = TODO.objects.all()
        if username:
            todos = todos.filter(creator__username=username)
        return todos


# class UserUpdateMutation(graphene.Mutation):
#
#     class Arguments:
#         first_name = graphene.String(required=True)
#         id = graphene.ID()
#
#     user = graphene.Field(UserType)
#
#     @classmethod
#     def mutate(cls, root, info, first_name, id):
#         user = User.objects.get(id=id)
#         user.first_name = first_name
#         user.save()
#         return UserUpdateMutation(user=user)

# class UserCreateMutation(graphene.Mutation):
#
#     class Arguments:
#         username = graphene.String()
#         first_name = graphene.String()
#         last_name = graphene.String()
#
#     user = graphene.Field(UserType)
#
#     @classmethod
#     def mutate(cls, root, info, username, first_name, last_name):
#         user = User(username=username, first_name=first_name, last_name=last_name)
#         user.save()
#         return UserCreateMutation(user=user)
#
# class Mutations(ObjectType):
#
#     create_user = UserCreateMutation.Field()

class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id):
        User.objects.get(id=id).delete()

        return UserDeleteMutation(user=None)


class Mutations(ObjectType):
    delete_user = UserDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
