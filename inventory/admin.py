from django.contrib import admin

# Register your models here.
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'expiration_date', 'added_by')
    list_filter = ('unit', 'expiration_date')