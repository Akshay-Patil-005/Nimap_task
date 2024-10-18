# test.py
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Client, Project

class APITestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client.objects.create(client_name='Test Client', created_by=self.user)
        self.project = Project.objects.create(project_name='Test Project', client=self.client, created_by=self.user)
        self.api_client = APIClient()
        self.api_client.force_authenticate(user=self.user)

    def test_get_clients(self):
        # Test getting a list of clients
        response = self.api_client.get('/api/clients/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['client_name'], 'Test Client')

    def test_create_client(self):
        # Test creating a new client
        data = {'client_name': 'New Client'}
        response = self.api_client.post('/api/clients/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Client.objects.count(), 2)

    def test_get_client_detail(self):
        # Test getting client details
        response = self.api_client.get(f'/api/clients/{self.client.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['client_name'], 'Test Client')

    def test_create_project(self):
        # Test creating a new project under a client
        data = {'project_name': 'New Project', 'users': [{'id': self.user.id, 'name': self.user.username}]}
        response = self.api_client.post(f'/api/clients/{self.client.id}/projects/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Project.objects.count(), 2)
