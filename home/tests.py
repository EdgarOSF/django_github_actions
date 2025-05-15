from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    def test_home_view_status_code(self):
        """Test that the home view returns a 200 status code"""
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        """Test that the home view uses the correct template"""
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_view_context(self):
        """Test that the home view passes the correct context to the template"""
        response = self.client.get(self.home_url)
        self.assertIn('view', response.context)
        self.assertEqual(response.context['view'].template_name, 'home.html')
