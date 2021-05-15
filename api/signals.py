from django.db.models.signals import pre_save
from django.contrib.auth.models import User


def update_user(sender, instance, **kwargs):
    if instance.email != '':
        instance.username = instance.email

pre_save.connect(update_user, sender=User)