from django.core.mail import send_mail

from blog.models import Post


def send_blog_email(post_item: Post):
    send_mail(
        'Поздравляем',
        f'Запись блога {post_item.title} набрала 100 просмотров!',
        'vilkov-l-nn@yandex.ru',
        ['vilkov-l-nn@mail.ru'],
        fail_silently=False,
    )