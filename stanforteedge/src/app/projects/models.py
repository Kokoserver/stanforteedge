from uuid import uuid4
from tortoise import models, fields

class Project(models.Model):
    id = fields.UUIDField(primary_key=True, default=uuid4)
    name = fields.CharField(max_length=100, unique=True)
    description = fields.TextField()
    image_url = fields.CharField(max_length=200, unique=True)
    facebook_url = fields.CharField(max_length=300, unique=True)
    twitter_url = fields.CharField(max_length=300, unique=True)
    instagram_url = fields.CharField(max_length=300, unique=True)
    youtube_url = fields.CharField(max_length=300, unique=True)
    website_url = fields.CharField(max_length=300, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)