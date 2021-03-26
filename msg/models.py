from django.db import models
from django.contrib.auth import get_user_model
from .tasks import celery_task
from django.db import transaction

User = get_user_model()

# Create your models here.
class Message(models.Model):
    user           = models.ForeignKey(User, verbose_name='User', on_delete = models.CASCADE, default=1)
    header         = models.TextField(verbose_name='Header', max_length=200)
    body           = models.TextField(verbose_name='Body', max_length=2000)
    delivered_flag = models.BooleanField(verbose_name='Delivered flag', default=False)
    read_flag      = models.BooleanField(verbose_name='Read flag', default=False)
    created_at     = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at     = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        transaction.on_commit(lambda: celery_task.delay(self.id))