from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from time import sleep
from school_districts.models import StateMap

class TestBasicPovertyMap(StaticLiveServerTestCase):

    fixtures = ["states"]

    def setUp(self):
        self.url = f"{self.live_server_url}/schools/PA"
        self.browser = Chrome()
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_webpage_has_map(self):
        # navigate to the page
        response = self.browser.get(self.url)
        # check title
        pa = StateMap.objects.get(state="PA")
        self.assertEqual(self.browser.title, "PA School District Poverty Map")
        # check that map exists
        sleep(10)
        self.browser.find_element(By.ID, "State-Map")