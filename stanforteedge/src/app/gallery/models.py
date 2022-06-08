from tortoise.models import Model
from tortoise import fields


class Gallery(Model):
    name = fields.CharField(max_length=100, unique=True)
    url = fields.CharField(max_length=200, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
