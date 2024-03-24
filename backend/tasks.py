from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def send_email_task(subject, message, to):
    """
    A Celery task to send an email.
    """
    msg = EmailMultiAlternatives(
        # title:
        subject,
        # message:
        message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        to
    )
    msg.send()
