from django.test import TestCase
from django.urls import reverse
from school_districts.models import StateMap

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
        self.assertIsInstance(response.context["GeoData"], StateMap)