from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid
class YGBaseModel(models.Model):
    id = models.CharField(primary_key=True,
                          verbose_name='ID')
    class Meta:
        abstract = True

@receiver(pre_save)
def new_uuid_value(sender,**kwargs):
    if issubclass(sender,YGBaseModel):
        isinstance = kwargs.get('instance')
        if isinstance.id is None:
            isinstance.id = uuid.uuid4().hex
