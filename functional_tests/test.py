from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestBasicPovertyMap(StaticLiveServerTestCase):

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
        self.assertEqual(self.browser.title, "PA School District Poverty Map")
        # check that map exists
        self.browser.find_element(By.ID, "State-Map")