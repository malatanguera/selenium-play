#all the stuff to import - mostly boilerplate, tho I think we'll add to it later in the process
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create the class, call it whatever
class PythonDoTheThingSearchWhatever(unittest.TestCase): #remember your colons:

    def setUp(self):
        self.driver = webdriver.Firefox() #to test in firefox. add other browser info when I actually find it

#this name must start with the four letters 'test'. after that call it whatever
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://base URL here.com") #navigate to page
        self.assertIn("Python", driver.title) #code code code... this is checking the title. do whatever you need
        elem = driver.find_element_by_name("name here from html element inspection") #find by name or by id, always use (" ")
        element.clear() #clears a text field before you send keys to it
        element.send_keys("text field entry here")
        element.send_keys(Keys.ENTER) #sends keyboard keys, like imported above. can send keys on any element, possible to test keyboard shortcuts, etc



#closes the browser
    def tearDown(self):
        self.driver.close()

#ending boilerplate. these are double _ _ 
if __name__ == "__main__":
    unittest.main()
