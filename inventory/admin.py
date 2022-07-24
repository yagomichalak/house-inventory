from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_diplay = ("name", "quantity", "price", "category_name")