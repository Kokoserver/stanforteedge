from uuid import uuid4
from tortoise import models, fields



class Gallery(models.Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    name = fields.CharField(max_length=100, unique=True)
    url = fields.CharField(max_length=200, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
