# Django + DynamoDB Backend Project

This project is a Django application that uses AWS DynamoDB for storage. It is designed to be deployed using Docker and Docker Compose.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Common Issues](#common-issues)

## Project Overview
This project includes:
- A Django application
- AWS DynamoDB for data storage
- Docker and Docker Compose for containerization

## Installation

### 1. Create a .env file
```plaintext
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
S3_BUCKET_NAME=your_s3_bucket_name
OPENAI_API_KEY=your_openai_api_key

DYNAMODB_ENDPOINT_URL=http://dynamodb:8000
AWS_REGION=us-west-2
```

### 2. Build and start Docker containers
```bash
docker-compose up --build -d
```

### 3. Access the Django application
http://34.219.2.232:8001
