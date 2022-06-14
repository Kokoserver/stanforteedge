from tortoise import models, fields


class User(models.Model):
    email = fields.CharField(max_length=150, unique=True, blank=False)
    username = fields.CharField(max_length=150, unique=True, blank=True)
    password = fields.CharField(max_length=300, blank=False)
    is_active = fields.BooleanField(default=False)
    is_validated = fields.BooleanField(default=False)
    is_admin = fields.BooleanField(default=False)
    is_super_admin = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DatetimeField(auto_now=True)
