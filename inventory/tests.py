from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from users.models import CustomUser
from inventory.models import InventoryItem

class InventoryTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="password123")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.inventory_url = "/api/inventory/"

    def test_create_inventory_item(self):
        data = {
            "name": "Milk",
            "quantity": 2,
            "unit": "liters",
            "expiration_date": "2025-01-15"
        }
        response = self.client.post(self.inventory_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InventoryItem.objects.count(), 1)
        self.assertEqual(InventoryItem.objects.first().name, "Milk")

    def test_list_inventory_items(self):
        InventoryItem.objects.create(name="Eggs", quantity=12, unit="pieces", expiration_date="2025-01-10", added_by=self.user)
        response = self.client.get(self.inventory_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Eggs")

    def test_update_inventory_item(self):
        item = InventoryItem.objects.create(name="Butter", quantity=1, unit="kg", expiration_date="2025-02-01", added_by=self.user)
        update_data = {
            "name": "Butter",
            "quantity": 2,
            "unit": "kg",
            "expiration_date": "2025-02-10"
        }
        response = self.client.put(f"{self.inventory_url}{item.id}/", update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item.refresh_from_db()
        self.assertEqual(item.quantity, 2)

    def test_delete_inventory_item(self):
        item = InventoryItem.objects.create(name="Cheese", quantity=1, unit="kg", expiration_date="2025-03-01", added_by=self.user)
        response = self.client.delete(f"{self.inventory_url}{item.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InventoryItem.objects.count(), 0)

    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.inventory_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

