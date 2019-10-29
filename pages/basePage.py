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


class BasePageClass():
	def __init__(self,driver):
		self.driver = driver

class HomePageClass():
	def __init__(self,driver):
		self.driver = driver
		self.search_bar = self.driver.find_element_by_xpath(HomePageLocators.search_bar_xpath)

	
	def enter_search_term(self):
		self.search_bar.send_keys("python/cpython")
		self.search_bar.click() 
		self.driver.implicitly_wait(20)

	def click_searh_repo(self):
		self.search_bar.send_keys(Keys.RETURN) 

class SearchPageClass(BasePageClass):
	def __init__(self,driver):
		self.driver = driver
		self.repo_list = self.driver.find_elements_by_xpath(Search_Repo_Page_Locators.pick_repo_xpath)
		#self.chose_right_repo = self.driver.find_element_by_xpath(Search_Repo_Page_Locators.find_link_of_repo)  
	
	def search_for_the_repo_name(self):
		for items in self.repo_list: 
			self.link_of_repo = items.find_element_by_css_selector(Search_Repo_Page_Locators.find_link_of_repo)
			print(self.link_of_repo.text) 
			self.driver.implicitly_wait(20)
			if self.link_of_repo.text == "python/cpython": 
				self.link_of_repo.click()
				break   





		


