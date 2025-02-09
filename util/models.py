from django.db import models



import uuid


class UserAction(models.Model):
    id =models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    user_id =models.CharField(default="",max_length=266)
    title =models.CharField(max_length=256,null=True)
    describe =models.CharField(max_length=256,null=True)
    time =models.DateTimeField(null=True)
