from rest_framework import serializers
from todos.models import Todo
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ['id', 'owner', 'text', 'status']


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todos']
