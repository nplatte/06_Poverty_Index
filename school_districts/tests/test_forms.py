from django.test import TestCase
from school_districts.forms import DistrictDataUploadForm
from django.core.files.uploadedfile import SimpleUploadedFile

class TestDataUploadForm(TestCase):

    def setUp(self):
        self.form = DistrictDataUploadForm

        path = "school_districts\\state_data\\ussd23.xls"
        ofile = open(path, 'rb')
        self.post_data = {"file": "File"}
        self.file_data = {'state_data': SimpleUploadedFile(ofile.name, ofile.read())}
        return super().setUp()
    
    def test_good_data_is_valid(self):
        f = self.form(self.post_data, self.file_data)
        self.assertTrue(f.is_valid())

    def test_requires_file(self):
        f = self.form({}, {})
        self.assertFalse(f.is_valid())