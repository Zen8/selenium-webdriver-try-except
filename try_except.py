import unittest

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

class ValidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="[Chrome driver path]")
        self.driver.get("URL to open")
        
    def valid_login(self):
        driver=self.driver
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keeys("password")
    try:
        driver.find_element_by_id("btnLogin").click()
    except NoSuchElementException as exception:
        print ("Element not found and test failed")
        
    def tearDown(self):
        self.driver.quit()
    
if _name_== '_main_':
    unittest.main()
