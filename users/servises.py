from django.core.mail import send_mail

from users.models import User


def send_confirm_email(parent: User):
    send_mail(
        'Поздравляем! Вы зарегистрировались на нашем сайте.',
        f'Ваша почта  {parent.email} должна быть подтверждена. После подтверждения Вы сможете авторизоваться на сайте.',
        'vilkov-l-nn@yandex.ru',
        [f'{parent.email}'],
        fail_silently=False,
    )