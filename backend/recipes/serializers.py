from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    posterId = serializers.CharField(max_length=255)
    content = serializers.CharField()
