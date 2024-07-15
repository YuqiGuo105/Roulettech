import uuid

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def create_recipe_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Recipes',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table


def load_sample_recipes(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Recipes')

    recipes = [
        {
            'id': str(uuid.uuid4()),
            'name': 'Spaghetti Bolognese',
            'posterId': '123',
            'imageURL': 'https://www.slimmingeats.com/blog/wp-content/uploads/2010/04/spaghetti-bolognese-36-720x720.jpg',
            'content': 'Delicious spaghetti with a rich Bolognese sauce.'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Chicken Curry',
            'posterId': '124',
            'imageURL': 'https://www.foodandwine.com/thmb/8YAIANQTZnGpVWj2XgY0dYH1V4I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/spicy-chicken-curry-FT-RECIPE0321-58f84fdf7b484e7f86894203eb7834e7.jpg',
            'content': 'Aromatic chicken curry with a blend of spices.'
        },
        {
            'id': str(uuid.uuid4()),
            'name': 'Beef Stew',
            'posterId': '125',
            'imageURL': 'https://s23209.pcdn.co/wp-content/uploads/2020/03/Best-Ever-Beef-StewIMG_1367.jpg',
            'content': 'Hearty beef stew with tender pieces of beef and vegetables.'
        }
    ]

    for recipe in recipes:
        try:
            table.put_item(Item=recipe)
            print(f"Inserted recipe: {recipe['name']}")
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Credentials error: {e}")
        except Exception as e:
            print(f"Error inserting recipe: {e}")


if __name__ == '__main__':
    recipe_table = create_recipe_table()
    print("Table status:", recipe_table.table_status)

    load_sample_recipes()
