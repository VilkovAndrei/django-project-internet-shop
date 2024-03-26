from django.core.management import BaseCommand
import json

from catalog.models import Product, Category
from config.settings import FILL_JSON_FILE


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():

        try:
            with open(FILL_JSON_FILE, "r", encoding="utf-8") as file:
                list_json = json.load(file)
        except FileNotFoundError:
            print(f'Файл {FILL_JSON_FILE} не найден!')

        category_json = [x for x in list_json if x['model'] == 'catalog.category']
        return category_json

    @staticmethod
    def json_read_products():
        try:
            with open(FILL_JSON_FILE, "r", encoding="utf-8") as file:
                list_json = json.load(file)
        except FileNotFoundError:
            print(f'Файл {FILL_JSON_FILE} не найден!')

        product_json = [x for x in list_json if x['model'] == 'catalog.product']
        return product_json

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'], name=category['fields']['name'], description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'], name=product['fields']['name'], description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at']
                        )
            )

        Product.objects.bulk_create(product_for_create)
