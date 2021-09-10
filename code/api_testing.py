import selenium, time, unittest, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


CHROME_PATH = "/Users/nicholausbrell/python/selenium/chromedriver"

chrome_options = Options()
chrome_options.headless = True

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
    
    """
    Test for login for a user that does NOT exists.
    """
    def test_login_page_non_exsisting(self):
        driver = self.driver
        driver.get("http://localhost/login")
        
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        
        username.send_keys("nonExsistingUser")
        password.send_keys("123")
        
        password.send_keys(Keys.RETURN)
        
        # if the user enters the incorrect password, the message "Incorrect password."
        # would be returned to the user in JSON format.
        #assert "Incorrect password." not in driver.page_source
        
        # if the user tries to login using a username that does not exsists,
        # the message "user <username> does not exists" would be returned to the user
        # in JSON format.
        assert "does not exists" in driver.page_source
    
    """
    Test login for a user that does exists, but enters the INCORRECT password.
    """
    def test_login_fail(self):
        driver = self.driver
        driver.get("http://localhost/login")
        
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        
        username.send_keys("nick")
        password.send_keys("wrongPassword")
        
        password.send_keys(Keys.RETURN)
        
        # if the user enters the incorrect password, the message "Incorrect password."
        # would be returned to the user in JSON format.
        assert "Incorrect password." in driver.page_source
    
    """
    Test login for a user that does exists, and enters the correct username 
    and password.
    """
    def test_login_success(self):
        driver = self.driver
        driver.get("http://localhost/login")
        
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        
        username.send_keys("nick")
        password.send_keys("123")
        
        password.send_keys(Keys.RETURN)
        
        # when a user 'logs in' using the correct credentials, the message
        # "logged in as <username>" will be returned to the user in JSON format.
        assert "logged in as" in driver.page_source
        
    '''
    def test_signup_page(self):
        driver = self.driver
        driver.get("http://localhost/signup")
        
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        
        username.send_keys("test_user1")
        
        password.send_keys("123")
        password.send_keys(Keys.RETURN)
        
        # if the user selects chooses a username that is already taken, the message
        # "<username> is already taken." would be returned to the user in JSON format.
        assert "is already taken." not in driver.page_source
    '''

    """
    Test for changing a password for a user that does NOT exsist.
    """
    def test_change_pw_non_exsisting(self):
        driver = self.driver
        driver.get("http://localhost/changepassword")
        
        username     = driver.find_element_by_name("username")
        old_password = driver.find_element_by_name("old_password")
        new_password = driver.find_element_by_name("new_password")
        
        username.send_keys("nonExsistingUser")
        old_password.send_keys("123")
        new_password.send_keys("123")
        
        new_password.send_keys(Keys.RETURN)
        
        # if the user tries to change the password for a username 
        # that does not exsists, the message "user <username> does not exists" 
        # would be returned to the user in JSON format.
        assert "does not exists" in driver.page_source
    
    """
    Test for changing the password for a user that does exists, but enters 
    the INCORRECT 'old_password'.
    """
    def test_change_pw_fail(self):
        driver = self.driver
        driver.get("http://localhost/changepassword")
        
        username     = driver.find_element_by_name("username")
        old_password = driver.find_element_by_name("old_password")
        new_password = driver.find_element_by_name("new_password")
        
        username.send_keys("nick")
        old_password.send_keys("1234")
        new_password.send_keys("123")
        
        new_password.send_keys(Keys.RETURN)
        
        # if the 'old_password' (aka current password) is incorrect, the message
        # "password does not match your old password" would be returned to the user
        # in JSON format. 
        assert "password does not match your old password" in driver.page_source
    
    """
    Test for successfully changing an exsisting users password.
    """
    def test_change_pw_success(self):
        driver = self.driver
        driver.get("http://localhost/changepassword")
        
        username     = driver.find_element_by_name("username")
        old_password = driver.find_element_by_name("old_password")
        new_password = driver.find_element_by_name("new_password")
        
        username.send_keys("nick")
        old_password.send_keys("123")
        new_password.send_keys("123")
        
        new_password.send_keys(Keys.RETURN)
        
        # if the user successfully updates their password, the message
        # "success. Changed password from '<old_password>' to '<new_password>'" will
        # be returned to the user in JSON format.
        assert "success" in driver.page_source
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

