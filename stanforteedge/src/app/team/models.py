from tortoise import models, fields
from uuid import uuid4

class Team(models.Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    name = fields.CharField(max_length=100, unique=True)
    position = fields.CharField(max_length=100, unique=True)
    description = fields.TextField()
    image_url = fields.CharField(max_length=200, unique=True)
