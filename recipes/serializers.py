from rest_framework import serializers
from .models import RecipeItem

class RecipeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeItem
        fields = '__all__'
