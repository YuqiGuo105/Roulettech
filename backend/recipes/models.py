# myapp/models.py
import uuid

from django.db import models


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    posterId = models.CharField(max_length=255)
    imageURL = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.name
