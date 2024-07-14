import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table_name = 'Recipes'

try:
    # Check if the table already exists
    table = dynamodb.Table(table_name)
    table.load()  # Load the table to check if it exists
    print(f"Table '{table_name}' already exists.")

except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        # Table does not exist, so create it
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
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

        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        print(f"Table '{table_name}' created successfully.")
    else:
        # Some other error occurred
        print(f"Error occurred: {e.response['Error']['Message']}")
