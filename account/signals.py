from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.core.mail import send_mail

@receiver(post_save,sender=User)
def todo_post_save_action(*args, **kwargs):
    if kwargs.get('created'):
        obj = kwargs.get('instance')
        print(obj.email)
        subject = 'Welcom'
        msg = 'Welcome'
        receivers = [obj.email]
        send_mail(subject=subject, message=msg, from_email='notifiersys@gmail.com', recipient_list=receivers)
