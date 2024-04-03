from django.contrib import admin
from catalog.models import Category, Product, Our_contact


@admin.register(Our_contact)
class OurContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'country', 'inn', 'address', 'phone', 'email',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
