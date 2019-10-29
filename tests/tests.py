import unittest
import HtmlTestRunner
from selenium import webdriver
 
import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir +'/locators')
sys.path.insert(0, parentdir +'/pages')

from locators import HomePageLocators
from basePage import HomePageClass 
from basePage import SearchPageClass

# This is the TEST GITHUB SEARCH BASE class 
class TEST_GITHUB_SEARCH_BASE(unittest.TestCase): 
	#we set up the test scenario here
	@classmethod  
	def setUp(self): 
		self.driver  = webdriver.Chrome(parentdir + "/chromedriver.exe")  
		self.driver.get("https://github.com/") 
		print("We are on the home page")
		self.driver.maximize_window()

#in this test case we test if the home page have loaded succefully
	def test_home_page_loaded_successfully(self):
		driver = self.driver
		self.assertEqual("The world’s leading software development platform · GitHub", driver.title)

#in this test case , we check if search term was added succefully
	def test_entering_search_term(self):
		driver = self.driver 
		homepagecaller = HomePageClass(driver) 
		homepagecaller.enter_search_term()
		search_bar_element = self.driver.find_element_by_xpath(HomePageLocators.search_bar_xpath)
		self.assertEqual("python/cpython" , search_bar_element.get_attribute("value") )  
		
 
#in this test case we test you get redirected to the repo search page after you click enter for the search term 
	def test_redirecting_to_repo_search_page(self): 
		driver = self.driver 
		homepagecaller = HomePageClass(driver)
		homepagecaller.enter_search_term()
		homepagecaller.click_searh_repo()
		self.assertEqual("Search · python/cpython · GitHub" , self.driver.title)
   
#in this test case we Test if you find your search result and get redirected to the repo page  
	def test_chose_the_repo(self):
		driver = self.driver
		homepagecaller = HomePageClass(driver)  
		homepagecaller.enter_search_term()
		homepagecaller.click_searh_repo()
		searchpagecaller = SearchPageClass(driver)
		searchpagecaller.search_for_the_repo_name() 
		self.assertEqual("https://github.com/python/cpython", self.driver.current_url)  


#here we launch the teardown method for the test scenario
	@classmethod 
	def tearDown(self):
		self.driver.close()
		self.driver.quit()
 
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=parentdir + '/Reports')) 
     
	  