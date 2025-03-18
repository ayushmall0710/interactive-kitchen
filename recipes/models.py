from django.db import models
from users.models import CustomUser
# from django.contrib.postgres.fields import JSONField  # For PostgreSQL; use models.JSONField for Django >= 3.1

class Recipe(models.Model):
    name = models.CharField(max_length=255)  # Recipe name
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="recipes")  # User who saved the recipe
    cuisine = models.CharField(max_length=100, blank=True, null=True)  # Cuisine type
    spicy_level = models.CharField(max_length=50, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")], default="Medium")  # Spicy level
    cooking_time = models.IntegerField()  # Cooking time in minutes
    instructions = models.TextField()  # Recipe instructions
    ingredients = models.JSONField()  # Ingredients as a JSON object
    created_at = models.DateTimeField(auto_now_add=True)  # When the recipe was saved

    def __str__(self):
        return f"{self.name} ({self.user.username})"
