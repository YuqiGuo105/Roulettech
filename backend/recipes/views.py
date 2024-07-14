from django.http import HttpResponse  # Add this import
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
            table.put_item(Item=serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk):
    try:
        response = table.get_item(Key={'id': pk})
        recipe = response['Item']
    except KeyError:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            table.put_item(Item=serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        table.delete_item(Key={'id': pk})
        return Response(status=status.HTTP_204_NO_CONTENT)
