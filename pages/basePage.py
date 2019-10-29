import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir +'/locators')


from locators import HomePageLocators 
from locators import Search_Repo_Page_Locators



# Here for the Home Page Class : we define all functions for the home page, all functions that work with home page elements
class HomePageClass():
	#initialize a constructor
	def __init__(self,driver): 
		# We call the driver
		self.driver = driver 
		# we define the locator that we will call in more than one function here which is the search bar locator
		self.search_bar = self.driver.find_element_by_xpath(HomePageLocators.search_bar_xpath)

	#in this function we enter the search term through the search bar
	def enter_search_term(self):
		self.search_bar.send_keys("python/cpython")
		self.search_bar.click() 
		self.driver.implicitly_wait(20)


    #in this function here, we click enter to continue our search
	def click_searh_repo(self):
		self.search_bar.send_keys(Keys.RETURN) 


 

# Here for the search page class: we dfine all the functions that we will need inside the search page 
class SearchPageClass():
	#initialize a constructor
	def __init__(self,driver):
		# We call the driver
		self.driver = driver
		# we define the locator that we will use to select the list of repos that was listed after our search
		self.repo_list = self.driver.find_elements_by_xpath(Search_Repo_Page_Locators.pick_repo_xpath)


	# in this function, I go through eveyrylist item and check for the link of the repo, and if the link matches our search term, I break the if statment.
	def search_for_the_repo_name(self):
		for items in self.repo_list: 
			self.link_of_repo = items.find_element_by_css_selector(Search_Repo_Page_Locators.find_link_of_repo) 
			self.driver.implicitly_wait(20) 
			if self.link_of_repo.text == "python/cpython": 
				self.link_of_repo.click()
				break   





		


