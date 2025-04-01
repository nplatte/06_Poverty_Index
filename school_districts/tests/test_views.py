from django.test import TestCase
from django.urls import reverse

class TestStateView(TestCase):

    def setUp(self):
        self.url = reverse("school_poverty_state_view")
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_GET_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_correct_context_passed(self):
        response = self.client.get(self.url)
        self.assertIn("GeoData", response.context)