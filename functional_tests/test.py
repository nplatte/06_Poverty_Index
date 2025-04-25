from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from time import sleep
from django.urls import reverse
from school_districts.models import StateMap

class TestBasicPovertyMap(StaticLiveServerTestCase):

    fixtures = ["states"]

    def setUp(self):
        self.url = f"{self.live_server_url}{reverse('school_poverty_state_view')}"
        self.browser = Chrome()
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_webpage_has_map(self):
        # navigate to the page
        response = self.browser.get(self.url)
        # check title
        pa = StateMap.objects.get(state="PA")
        self.assertEqual(self.browser.title, "PA State Map")
        # check that map exists
        self.browser.find_element(By.ID, "State-Map")


class TestUploadDataFile(StaticLiveServerTestCase):

    def setUp(self):
        self.url = f"{self.live_server_url}{reverse('add_state_data')}"
        self.browser = Chrome()

    def test_upload_data_file_to_server(self):
        # Go to the site
        self.response = self.browser.get(self.url)
        # click the file upload button 
        file_upload = self.browser.find_element(By.ID, "file-upload")
        file_upload.send_keys("")
        submit_btn = self.browser.find_element(By.ID, "submit-btn")
        submit_btn.click()
        # upload the file to the server
        # the page redirects you to the map 
        self.assertEqual(self.browser.title, "PA State Map")