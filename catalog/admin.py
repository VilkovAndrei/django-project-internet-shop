from django.contrib import admin
from catalog.models import Category, Product, OurContact, Version


@admin.register(OurContact)
class OurContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'inn', 'address', 'phone', 'email',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'product', 'current_version')
    list_filter = ('product',)
    search_fields = ('name',)
