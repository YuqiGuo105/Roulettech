import uuid
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import RecipeSerializer
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('Recipes')


def index(request):
    return HttpResponse("Welcome to the Recipe API. Navigate to /api/recipes/ to use the API.")


@api_view(['GET', 'POST'])
def recipe_list(request):
    if request.method == 'GET':
        response = table.scan()
        return Response(response['Items'])

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            # Generate a unique ID for the new recipe
            recipe_data = serializer.validated_data
            recipe_data['id'] = str(uuid.uuid4())
            try:
                table.put_item(Item=recipe_data)
                return Response(recipe_data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    try:
        response = table.get_item(Key={'id': pk})
        recipe = response.get('Item')
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            recipe_data = serializer.validated_data
            recipe_data['id'] = pk  # Ensure the ID remains the same
            try:
                table.put_item(Item=recipe_data)
                return Response(recipe_data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            table.delete_item(Key={'id': pk})
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
