from django.test import TestCase
from django.urls import reverse
from school_districts.models import StateMap
from django .http import JsonResponse

class TestStateView(TestCase):
    
    fixtures = ["states"]

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
        self.assertEqual(type(response.context["GeoData"].map), dict)

class TestGETStateMap(TestCase):

    fixtures = ["test_states"]

    def setUp(self):
        self.response = self.client.get(reverse("state_map"))
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_GET_returns_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_returns_JSON(self):
        self.assertIsInstance(self.response, JsonResponse)

    def test_returns_data(self):
        self.assertEqual(self.response.json()["schools"], 2)