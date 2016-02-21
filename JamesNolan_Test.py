from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from github import Github

g = Github("JamesNolanTest", "jamesnolantest1")

repo = g.get_user().get_repo("jamesnolantest")
print repo.name
milestone = repo.get_milestone(1)
label = "bug"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_page_loads_Pass(self):
        try:
            print "Start Test - test_page_loads_Pass"
            driver = self.driver
            print "Navigate to 'http://www.google.com'"
            driver.get("http://www.google.com")
            print "Assertion:  Title = Google"
            self.assertIn("Google", driver.title)
            print "Assertion: Find Element by name 'q'.  (Search Bar)"
            elem = driver.find_element_by_name("q")
            print "Type 'google search'"
            elem.send_keys("google search")
            print "'Press Enter Key'"
            elem.send_keys(Keys.RETURN)            
            print "End Test - test_page_loads_Pass"
        except AssertionError:
            repo.create_issue("test_page_loads_Pass","Error in 'test_page_loads_Pass'","JamesNolanTest",milestone,label)
            print "Issue logged for test - test_page_loads_Pass"

    def test_page_loads_IntentionalFail(self):
        try:
            print "Start Test - test_page_loads_IntentionalFail"
            driver = self.driver
            print "Navigate to 'http://www.googte.com'"
            driver.get("http://www.googte.cm")
            print "Assertion:  Title = Google"
            self.assertIn("Google", driver.title)
            print "Assertion: Find Element by name 'q'.  (Search Bar)"
            elem = driver.find_element_by_name("q")
            print "Type 'google search'"
            elem.send_keys("google search")
            print 'Press Enter Key'
            elem.send_keys(Keys.RETURN)            
            print "End Test - test_page_loads_IntentionalFail"
        except AssertionError:
            repo.create_issue("test_page_loads_IntentionalFail","Error in 'test_page_loads_IntentionalFail' \n The url failed to load correctly.  \n \n *Auto Generated from Selenium","JamesNolanTest",milestone,label)            
            print "Issue logged for test - test_page_loads_IntentionalFail"

    def test_duck_fullValidation(self):
        try:
            print "Start Test - test_duck_fullValidation"
            driver = self.driver
            print "Navigate to 'https://duckduckgo.com/'"
            driver.get("https://duckduckgo.com/")
            print "Assertion: Title = DuckDuckGo"
            self.assertEqual("DuckDuckGo", driver.title)
            print "Assertion: Element present - logo_homepage_link.    (Homepage Logo)"
            self.assertTrue(self.is_element_present(By.ID, "logo_homepage_link"))
            print "Assertion: Element present - search_form_input_homepage.    (Search Bar)"
            self.assertTrue(self.is_element_present(By.ID, "search_form_input_homepage"))
            print "Assertion: Element present - Link Text 'Learn More."
            self.assertTrue(self.is_element_present(By.LINK_TEXT, "Learn More"))
            print "Assertion: Element present - search_button_homepage.    (Search Button)"
            self.assertTrue(self.is_element_present(By.ID, "search_button_homepage"))            
            print "End Test - test_duck_fullValidation"
        except AssertionError:
            repo.create_issue("test_duck_fullValidation","Error in 'test_duck_fullValidation' \n \n *Auto Generated from Selenium","JamesNolanTest",milestone,label)            
            print "Issue logged for test - test_duck_fullValidation"

    def test_duck_IncorrectSearchBarID(self):
        try:
            print "Start Test - test_duck_IncorrectSearchBarID"
            driver = self.driver
            print "Navigate to 'https://duckduckgo.com/'"
            driver.get("https://duckduckgo.com/")
            print "Assertion: Title = DuckDuckGo"
            self.assertEqual("DuckDuckGo", driver.title)
            print "Assertion: Element present - logo_homepage_link.    (Homepage Logo)"
            self.assertTrue(self.is_element_present(By.ID, "logo_homepage_link"))
            print "Assertion: Element present - search_form_input_home.    (Search Bar)"
            self.assertTrue(self.is_element_present(By.ID, "search_form_input_home"))
            print "Assertion: Element present - Link Text 'Learn More."
            self.assertTrue(self.is_element_present(By.LINK_TEXT, "Learn More"))
            print "Assertion: Element present - search_button_homepage.    (Search Button)"
            self.assertTrue(self.is_element_present(By.ID, "search_button_homepage"))            
            print "End Test - test_duck_IncorrectSearchBarID"
        except AssertionError:
            repo.create_issue("test_duck_IncorrectSearchBarID","Error in 'test_duck_IncorrectSearchBarID' \n The search ID Bar has been changed \n \n *Auto Generated from Selenium","JamesNolanTest",milestone,label)
            print "Issue logged for test - test_duck_IncorrectSearchBarID"

    def test_duck_buttonNotFound(self):
        try:
            print "Start Test - test_duck_buttonNotFound"
            driver = self.driver
            print "Navigate to 'https://duckduckgo.com/'"
            driver.get("https://duckduckgo.com/")
            print "Assertion: Title = DuckDuckGo"
            self.assertEqual("DuckDuckGo", driver.title)
            print "Assertion: Element present - logo_homepage_link.    (Homepage Logo)"
            self.assertTrue(self.is_element_present(By.ID, "logo_homepage_link"))
            print "Assertion: Element present - search_form_input_homepage.    (Search Bar)"
            self.assertTrue(self.is_element_present(By.ID, "search_form_input_homepage"))
            print "Assertion: Element present - Link Text 'Learn More."
            self.assertTrue(self.is_element_present(By.LINK_TEXT, "Learn More"))
            print "Navigate to Google.  Following Assertions expected to fail"
            driver.get("http://google.com")
            print "Assertion: Element present - search_button_homepage.    (Search Button)"
            self.assertTrue(self.is_element_present(By.ID, "search_button_homepage"))            
            print "End Test - test_duck_buttonNotFound"
        except AssertionError:
            repo.create_issue("test_duck_buttonNotFound","Error in 'test_duck_buttonNotFound' \n Unable to locate search button \n \n *Auto Generated from Selenium","JamesNolanTest",milestone,label)
            print "Issue logged for test - test_duck_buttonNotFound"

    def test_duck_timeDelayedElement(self):
        try:
            print "Start Test - test_duck_timeDelayedElement"
            driver = self.driver
            print "Navigate to 'https://duckduckgo.com/'"
            driver.get("https://duckduckgo.com/")
            print "Assertion: Title = DuckDuckGo"
            self.assertEqual("DuckDuckGo", driver.title)
            print "Assertion: Element present - logo_homepage_link.    (Homepage Logo)"
            self.assertTrue(self.is_element_present(By.ID, "logo_homepage_link"))
            print "Assertion: Element present - search_form_input_homepage.    (Search Bar)"
            self.assertTrue(self.is_element_present(By.ID, "search_form_input_homepage"))
            print "Find Link Text 'Take a Tour."
            for i in range(60):
                try:
                    if "Take a Tour." == driver.find_element_by_link_text("Take a Tour.").text: break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            print "End Test - test_duck_timeDelayedElement"
        except AssertionError:
            repo.create_issue("test_duck_timeDelayedElement","Error in 'test_duck_timeDelayedElement' \n \n *Auto Generated from Selenium","JamesNolanTest",milestone,label)
            print "Issue logged for test - test_duck_timeDelayedElement"

    def test_swrve_load(self):
        try:
            print "Start Test - test_swrve_load"
            driver = self.driver
            print "Navigate to 'https://www.swrve.com/"
            driver.get("https://www.swrve.com/")                        
            print "Assertion: Page Title = 'Swrve - Mobile Marketing Automation : Analytics, A/B ...'"
            self.assertEqual("Swrve - Mobile Marketing Automation : Analytics, A/B Testing, In-App Campaigns, Push Notifications", driver.title)
            print "Assertion: Get Started Today"
            self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Get Started Today')])[6]"))
            print "Click Get Started Today"
            driver.find_element_by_xpath("(//a[contains(text(),'Get Started Today')])[6]").click()
            print "Type 'Test First' into 'FirstName'"
            driver.find_element_by_id("FirstName").send_keys("Test First")
            print "Type 'Test Last' into 'LastName'"
            driver.find_element_by_id("LastName").send_keys("Test Last")
            print "Type 'testemail@email.com' into 'Email'"
            driver.find_element_by_id("Email").send_keys("testemail@email.com")
            print "Type '9876452100' into 'Phone'"
            driver.find_element_by_id("Phone").send_keys("9876452100")
            print "Type 'Testing Company' into 'Company'"
            driver.find_element_by_id("Company").send_keys("Testing Company")
            print "Click 'Swrve' Logo in the top left of the page"
            driver.find_element_by_css_selector("span.icon-swrve").click()        
            print "End Test - test_swrve_load"
        except AssertionError:
            repo.create_issue("test_swrve_load","Error in test 'test_swrve_load' \n \n *Auto Generated from Selenium ","JamesNolanTest",milestone,label)
            print "Issue logged for test - test_swrve_load"

    def test_surveyMonkey_Form_CatchWarnings(self):
        try:
            print "Start Test - test_surveyMonkey_Form_CatchWarnings"
            driver = self.driver
            print "Navigate to 'https://www.surveymonkey.com/"
            driver.get("https://www.surveymonkey.com/")          
            print "Click Link 'Sign up FREE'"
            driver.find_element_by_link_text("Sign Up FREE").click()
            print "Assertion: Element present. ID = 'username'"
            self.assertTrue(self.is_element_present(By.ID, "username"))            
            driver.find_element_by_id("username").clear()
            print "Type Test User into Username"
            driver.find_element_by_id("username").send_keys("Test User")
            print "Assertion: Element present. ID = 'password'"
            self.assertTrue(self.is_element_present(By.ID, "password"))            
            driver.find_element_by_id("password").clear()
            print "Typye 'Password' into password"
            driver.find_element_by_id("password").send_keys("Password")
            print "Assertion: Username warning present. No spaces"
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.missing"))
            print "Assertion: Password warning present. weak Password"
            self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='create_user_form']/fieldset[2]/ul/li[2]/span"))
            print "Assertion: Submit Form button present"
            self.assertTrue(self.is_element_present(By.ID, "submitform"))
            print "End Test - test_surveyMonkey_Form_CatchWarnings"
        except AssertionError:
            repo.create_issue("test_surveyMonkey_Form_CatchWarnings","Error in 'test_surveyMonkey_Form_CatchWarnings' \n \n *Auto Generated from Selenium","JamesNolanTest",milestone,label)
            print "Issue logged for test - test_surveyMonkey_Form_CatchWarnings"

    def test_surveyMonkey_Form_ExpectedFailed(self):
        try:
            print "Start Test - test_surveyMonkey_Form_ExpectedFailed"
            driver = self.driver
            print "Navigate to 'https://www.surveymonkey.com/"
            driver.get("https://www.surveymonkey.com/")                      
            print "Click Link 'Sign up FREE'"
            driver.find_element_by_link_text("Sign Up FREE").click()
            print "Assertion: Element present. ID = 'username'"
            self.assertTrue(self.is_element_present(By.ID, "username"))            
            driver.find_element_by_id("username").clear()
            print "Type Test_User_Testing_Sresu into Username"
            driver.find_element_by_id("username").send_keys("Test_User_Testing_Sresu")
            print "Assertion: Element present. ID = 'password'"
            self.assertTrue(self.is_element_present(By.ID, "password"))            
            driver.find_element_by_id("password").clear()
            print "Typye 'sdSDF234s' into password"
            driver.find_element_by_id("password").send_keys("sdSDF234s")
            print "Assertion: Submit Form button present"
            self.assertTrue(self.is_element_present(By.ID, "submitform"))
            print "Click Submit"
            driver.find_element_by_id("submitform").click()
            print "Assertion: 'Easily create your first survey' visible"
            self.assertTrue(self.is_element_present(By.ID, "create-title"))
            print "End Test - test_surveyMonkey_Form_ExpectedFailed"
        except AssertionError:
            repo.create_issue("test_surveyMonkey_Form_ExpectedFailed","Error in 'test_surveyMonkey_Form_ExpectedFailed' \n Vould not locate the Creation Title \n \n *Auto Generated from Selenium ","JamesNolanTest",milestone,label)
            print "Issue logged for test - test_surveyMonkey_Form_ExpectedWarningsFailed"

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
