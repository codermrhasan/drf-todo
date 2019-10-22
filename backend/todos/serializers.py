from rest_framework import serializers
from todos.models import Todo
from django.contrib.auth.models import User


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['url', 'id', 'owner', 'text', 'status']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'todos']
