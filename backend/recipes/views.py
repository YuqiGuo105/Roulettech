import os
import uuid
import openai
from botocore.client import Config, logger
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from backend import settings
from .serializers import RecipeSerializer
import boto3
from django.conf import settings

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


@api_view(['GET'])
@csrf_exempt
def get_presigned_url(request):
    s3_client = boto3.client(
        's3',
        region_name=settings.AWS_S3_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    file_name = request.GET.get('file_name')
    content_type = request.GET.get('content_type')

    if not file_name or not content_type:
        return JsonResponse({'error': 'file_name and content_type are required parameters'}, status=400)

    try:
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': file_name,
                'ContentType': content_type
            },
            ExpiresIn=3600
        )
        return JsonResponse({'presigned_url': presigned_url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
def generate_recipe(request):
    data = request.data
    prompt = data.get('prompt')

    if not prompt:
        return JsonResponse({'error': 'Prompt is required'}, status=400)

    openai.api_key = settings.OPENAI_API_KEY

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        recipe = response.choices[0].message['content'].strip()
        return JsonResponse({'recipe': recipe})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
