## Steps:

### Spin up a DynamoDB docker container
```docker run -p 8000:8000 -d amazon/dynamodb-local```


### Create a DynamoDB table
```python dynamodb.py```

### View the database table
```aws dynamodb list-tables --endpoint-url http://localhost:8000```

### Run the Django project
```python manage.py runserver 8081```
