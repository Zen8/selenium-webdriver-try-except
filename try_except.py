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

    
# Using try-except is the most common and natural way of handling unexpected errors 
# along with many more exception handling constructs.

#1. Arbitrary Exception

try:
    #your code
except Exception as ex:
    print(ex)

#2. Catch Multiple Exceptions in One Except Block

try:
    file = open('input-file', 'open mode')
except (IOError, EOFError) as e:
    print("Testing multiple exceptions. {}".format(e.args[-1]))

#Handle each exception in a dedicated block:

try:
    file = open('input-file', 'open mode')
except EOFError as ex:
    print("Caught the EOF error.")
    raise ex
except IOError as e:
    print("Caught the I/O error.")
    raise ex

#If you dont know what type of exception is thrown use the following:

try:
    file = open('input-file', 'open mode')
except:
    # In case of any unhandled error, throw it away
    raise
    
#3. Re-raising Exceptions. Exceptions once raised keep moving up to the calling methods until handled. 
You can add an except clause which could just have a [raise] call without any argument.

try:
    # Intentionally raise an exception.
    raise Exception('Why is it happening again?')
except:
    print("Entered in except.")
    # Re-raise the exception.
    raise
    
Output:
Entered in except.
Traceback (most recent call last):
  File "python", line 3, in <module>
Exception: Why is it happening again?
