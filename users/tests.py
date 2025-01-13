from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from users.models import CustomUser

# ----------------------
# Unit Tests for Users
# ----------------------
class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123",
            "date_of_birth": "2000-01-01"
        }

    def test_user_registration(self):
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_user_login(self):
        CustomUser.objects.create_user(username="testuser", password="testpassword123")
        response = self.client.post(reverse('login'), {
            "username": "testuser",
            "password": "testpassword123"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_logout(self):
        user = CustomUser.objects.create_user(username="testuser", password="testpassword123")
        self.token = Token.objects.create(user=user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        # self.client.force_authenticate(user=user)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)