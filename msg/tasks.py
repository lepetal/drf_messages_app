from celery.decorators import task
from django.apps import apps

@task
def celery_task(id):
    try:
        Message = apps.get_model(app_label='msg', model_name='Message')
        message = Message.objects.get(id=id)
    except ObjectDoesNotExist:
        message = None

    if message:
        message.delivered_flag = True
        message.save()