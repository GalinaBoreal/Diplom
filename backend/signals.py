from typing import Type

from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django_rest_passwordreset.signals import reset_password_token_created

from backend.models import ConfirmEmailToken, User
from .tasks import send_email_task

new_user_registered = Signal()

new_order = Signal()


# https://docs.djangoproject.com/en/5.0/topics/email/
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """
    Отправляем письмо с токеном для сброса пароля
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    return send_email_task.delay(
        subject=f"Password Reset Token for {reset_password_token.user}",
        message=reset_password_token.key,
        to=[reset_password_token.user.email]
    )


@receiver(post_save, sender=User)
def new_user_registered_signal(sender: Type[User], instance: User, created: bool, **kwargs):
    """
     отправляем письмо с подтверждением почты
    """
    if created and not instance.is_active:
        # send an e-mail to the user
        token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)
        return send_email_task.delay(
            subject=f"Password Email Token for {instance.email}",
            message=token.key,
            to=[instance.email]
        )


@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    отправляем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)
    return send_email_task.delay(
        subject=f"Обновление статуса заказа",
        message='Заказ сформирован',
        to=[user.email]
    )
