## Automation test task

This is a simple test on https://github.com/ website that searches for a repo via the search form on the gitgub top navigator,
checks if the repo shows in the test results and if you get redirected to the right repo when chosen.

**This test is written with python, tests are done by the unit testing framework. Using the selenium webdriver for browser automation.**

Comments are added inside lines of code for full details on functions.

Elements are mostly located via xpath and the css_selector.


## Project Design:
The project is divided in 4 folders:

1. Driver folder : Where I saved the installed version of chromedriver.exe
2. Tests folder : Where I added my tests.py file (You can run the tests locally from there).
3. Pages folder : this folder contains the basePage.py file where I stored all the pages classes ann related functions for each page.
4. Locators folder : This folder contains the locators.py class where I stored all the locators classes in locators.py
5. Reports folder : This folder is where I store my htmltestrunner reports with details around the passed/failed test cases.


## Cases covered :
* Testing if the home page have loaded succefully. (function name : test_home_page_loaded_successfully)
* Testing if search term was added succefully. (function name :test_entering_search_term )
* Testing if you get redirected to the repo search page after you click enter for the search term. (funtion name: test_redirecting_to_repo_search_page)
* Testing if you find your search result and get redirected to the repo page (function name : test_chose_the_repo)


## Requirements :
1. Make sure you install the compatibale chrome driver with your browser from here : https://chromedriver.chromium.org/ after you install it, remove the driver to the driver folder under liwwa_automation_test directory.
2. Make sure you have python installed, you can install it from here : https://www.python.org/downloads/
3. Make sure you install selenium driver for python from here : https://selenium-python.readthedocs.io/installation.html
This test runs on a windows P.C , MacOS


## How to run tests?
[![Build Status](https://travis-ci.com/rawaaqaffaf/liwwa-automation-test.svg?branch=master)](https://travis-ci.com/rawaaqaffaf/liwwa-automation-test)
[![codecov](https://codecov.io/gh/rawaaqaffaf/liwwa-automation-test/branch/master/graph/badge.svg)](https://codecov.io/gh/rawaaqaffaf/liwwa-automation-test)


open command line and change the directory to cloned_repository\liwwa_automation_test\tests.
run the tests by typing : `python tests.py`
