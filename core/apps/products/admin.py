from django.contrib import admin

from core.apps.products.models.products import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
