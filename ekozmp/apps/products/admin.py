from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "timestamp")
    search_fields = ["name"]

