import boto3
from django.conf import settings


def generate_presigned_url(file_name, file_type):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )

    try:
        response = s3_client.generate_presigned_url('put_object',
                                                    Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                                            'Key': file_name,
                                                            'ContentType': file_type},
                                                    ExpiresIn=3600)  # URL expires in 1 hour
    except Exception as e:
        return None

    return response
