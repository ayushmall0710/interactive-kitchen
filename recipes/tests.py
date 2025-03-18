from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import CustomUser
from recipes.models import Recipe

class RecipeTests(TestCase):
    def setUp(self):
        # Set up a test user and API client
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username="testuser", password="testpassword123")
        self.client.force_authenticate(user=self.user)

        # Sample recipe data
        self.recipe_data = {
            "name": "Cheesy Tomato Pasta",
            "cuisine": "Italian",
            "spicy_level": "Low",
            "cooking_time": 30,
            "instructions": "1. Cook pasta. 2. Prepare sauce. 3. Combine and serve.",
            "ingredients": [
                {"name": "Tomato", "quantity": 500, "unit": "g", "expiration_date": "2025-01-13"},
                {"name": "Cheese", "quantity": 200, "unit": "g", "expiration_date": "2025-02-02"},
                {"name": "Pasta", "quantity": 300, "unit": "g"}
            ]
        }

    def test_get_recipes(self):
        # Send a GET request to retrieve recipes
        response = self.client.get("/api/recipe/list/")
    
        # Assert the response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        # Assert the response contains a list of recipes
        self.assertIn("recipes", response.data)
        self.assertIsInstance(response.data["recipes"], list)
        
    def test_add_recipe_success(self):
        # Send a POST request to add a recipe
        response = self.client.post("/api/recipe/save/", self.recipe_data, format="json")

        # Assert the response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the response contains the recipe data
        self.assertIn("recipes", response.data)
        self.assertEqual(len(response.data["recipes"]), 1)
        self.assertEqual(response.data["recipes"][0]["name"], self.recipe_data["name"])

    def test_add_recipe_missing_field(self):
        # Remove the name field from the recipe data
        invalid_data = self.recipe_data.copy()
        del invalid_data["name"]

        # Send a POST request with invalid data
        response = self.client.post("/api/recipe/create/", invalid_data, format="json")

        # Assert the response status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Assert the error message
        self.assertIn("error", response.data)

    def test_add_recipe_unauthenticated(self):
        # Log out the user
        self.client.logout()

        # Send a POST request without authentication
        response = self.client.post("/api/recipe/create/", self.recipe_data, format="json")

        # Assert the response status
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Assert the error message
        self.assertIn("detail", response.data)
        self.assertEqual(response.data["detail"], "Authentication credentials were not provided.")

    def test_suggest_recipe(self):
        response = self.client.post(reverse('suggest_recipe'), self.recipe_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('recipe', response.data)
        self.assertGreaterEqual(len(response.data['recipe']), 3)