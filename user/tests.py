from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class CreateCustomerTests(TestCase):
    """
    tests create user
    """
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create_customer')
        self.valid_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'pays': 'Country',
            'role': 'CUSTOMER',
            'password': 'password'
        }

    def test_create_customer_success(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_customer_failure(self):
        invalid_data = {'email': 'invalid-email'}
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairViewTests(TestCase):
    """
    tests authenticate user
    """
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('token_obtain_pair')  # Assuming you name the URL pattern 'token_obtain_pair'
        self.user = get_user_model().objects.create_user(email='test@example.com', password='password')

    def test_token_obtain_pair_success(self):
        valid_credentials = {'email': 'test@example.com', 'password': 'password'}
        response = self.client.post(self.url, data=valid_credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_obtain_pair_failure(self):
        invalid_credentials = {'email': 'test@example.com', 'password': 'wrong-password'}
        response = self.client.post(self.url, data=invalid_credentials)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
