from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    expiration_date = models.DateField(null=True, blank=True)
    added_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='inventory_items')

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"