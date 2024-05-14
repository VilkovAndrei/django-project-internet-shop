from django.core.cache import cache

from catalog.models import Category, Product
from django.conf import settings


def get_categories_from_cache():
    # queryset = Category.objects.all()
    if not settings.CACHE_ENABLED:
        queryset = Category.objects.all()
        return queryset
    else:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = Category.objects.all()
            cache.set(key, cache_data)

        return cache_data

def get_products_from_cache():
    # queryset = Category.objects.all()
    if not settings.CACHE_ENABLED:
        queryset = Product.objects.all()
        return queryset
    else:
        key = 'products'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = Product.objects.all()
            cache.set(key, cache_data)

        return cache_data

# def cache_example():
#     if CACHE_ENABLED:
#         # Проверяем включенность кеша
#         key = f'students_list' # Создаем ключ для хранения
#         students_list = cache.get(key) # Пытаемся получить данные
#         if students_list is None:
#             # Если данные не были получены из кеша, то выбираем из БД и записываем в кеш
#             students_list = Student.objects.all()
#             cache.set(key, students_list)
#     else:
#         # Если кеш не был подключен, то просто обращаемся к БД
#         students_list = Student.objects.all()
#     # Возвращаем результат
#     return students_list
