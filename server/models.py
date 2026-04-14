from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    firstname = fields.CharField(max_length=100)
    lastname = fields.CharField(max_length=100)
    email = fields.CharField(max_length=255, unique=True)
    username = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=255)


class Workspace(Model):
    id = fields.IntField(pk=True)
    workspaceId = fields.CharField(max_length=255, unique=True)
    name = fields.CharField(max_length=100)
    password = fields.CharField(max_length=255)