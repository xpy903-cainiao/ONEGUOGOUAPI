import uuid
from django.db import models

class YGBaseModel(models.Model):
    id = models.CharField(max_length=50,primary_key=True,
                          verbose_name='ID')

    class Meta:
        abstract = True