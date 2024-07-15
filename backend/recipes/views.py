import os
import uuid

from botocore.client import Config
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from backend import settings
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


# views.py

@api_view(['GET'])
@csrf_exempt
def get_presigned_url(request):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        config=Config(signature_version='s3v4')
    )
    bucket_name = 'roulettech-photo-bucket'
    object_name = request.GET.get('file_name')
    content_type = request.GET.get('file_type', 'application/octet-stream')

    if not bucket_name:
        return JsonResponse({'error': 'S3 bucket name is not configured'}, status=500)
    if not object_name:
        return JsonResponse({'error': 'File name is required'}, status=400)

    try:
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={'Bucket': bucket_name, 'Key': object_name, 'ContentType': content_type},
            ExpiresIn=3600
        )
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f'Credentials error: {e}')
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        logger.error(f'Error generating presigned URL: {e}')
        return JsonResponse({'error': 'Error generating presigned URL'}, status=500)

    return JsonResponse({'url': presigned_url})

