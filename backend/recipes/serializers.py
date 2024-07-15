from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=255, read_only=True)  # Make the id field read-only
    name = serializers.CharField(max_length=255)
    posterId = serializers.CharField(max_length=255)
    imageURL = serializers.URLField(max_length=200)
    content = serializers.CharField()

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'posterId', 'imageURL', 'content']
