from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=100)
    status = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
