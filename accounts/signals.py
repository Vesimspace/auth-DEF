from django.contrib.auth.models import User
from accounts.models import Account, AccountStatus
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    print(instance.username, '__Created: ', created)
    if created:
       Account.objects.create(user=instance)

@receiver(post_save, sender=Account)
def create_status_message(sender, instance, created, **kwargs):
    if created:
       AccountStatus.objects.create(
           user_account = instance,
           status_message = f'{instance.user.username} joined!'
       )