from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import CustomUser

class RecipeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username="testuser", password="testpassword123")
        self.client.force_authenticate(user=self.user)
        self.recipe_data = {
            "ingredients": [
                {"name": "Tomato", "quantity": 500, "unit": "g", "expiration_date": "2025-01-13"},
                {"name": "Cheese", "quantity": 200, "unit": "g", "expiration_date": "2025-02-02"}
            ],
            "cuisine": "Italian",
            "spicy_level": "Low",
            "cooking_time": "30 minutes"
        }

    def test_suggest_recipe(self):
        response = self.client.post(reverse('suggest_recipe'), self.recipe_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('recipe', response.data)
        self.assertGreaterEqual(len(response.data['recipe']), 3)
