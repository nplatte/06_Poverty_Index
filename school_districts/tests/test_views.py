from django.test import TestCase
from django.urls import reverse
from school_districts.models import StateMap
from django .http import JsonResponse
from school_districts.forms import DistrictDataUploadForm
from django.core.files.uploadedfile import SimpleUploadedFile


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


class TestUploadData(TestCase):

    fixtures = ["test_states"]

    def setUp(self):
        self.url = reverse("add_state_data")

    def test_GET_returns_200(self):
        r = self.client.get(self.url)
        self.assertEqual(r.status_code, 200)

    def test_passes_corrrect_context(self):
        context = self.client.get(self.url).context
        self.assertIsInstance(context["form"], DistrictDataUploadForm)

    def test_valid_POST_redirects_to_map_page(self):
        path = "school_districts\\state_data\\ussd23.xls"
        ofile = open(path, "rb")
        file_data = {
            'state_data': SimpleUploadedFile(ofile.name, ofile.read())
        }
        response = self.client.post(self.url, file_data)
        self.assertRedirects(response, reverse("school_poverty_state_view"))
