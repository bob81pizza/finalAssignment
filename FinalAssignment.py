from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import unittest

class PythonTesting(unittest.TestCase):


	def setUp(self):
		self.driver = webdriver.Firefox()


	'''
	Navigate to the search page where no items are found. Try to click the search button again
	with no items in the search box. An pop-up error box should be displayed
	'''
	# def testNoInputSearchPage(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com/sr?origin=keywordsearch&contextualcategoryid=0&keyword=")
	# 	searchButton = driver.find_element_by_id("keyword-search-submit")
	# 	searchButton.click()
	# 	try:
	# 		alert = driver.switch_to.alert
	# 		a = alert.text
	# 		self.assertEqual(a,"Please specify a search term.")
	# 	except NoAlertPresentException:
	# 		self.fail("No alert is present")


	'''
	Navigate to the main page. Enter an item in the search box and use the 'Enter' key to
	initiage the search. Check to see that the URL has changed due to using the 'Enter' key
	'''
	# def testSearchByEnter(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com")
	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.send_keys("sock")
	# 	searchBox.send_keys(Keys.RETURN)
	# 	self.assertNotEqual(driver.current_url, "http://shop.nordstrom.com")


	'''
	Navigate to the main page. Enter the word 'sock' in the search box and use the 'Enter'
	key to initiate the search. Check to ensure that the first match has the word 'sock'
	in it.
	'''
	# def testSearchSock(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com")
	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.send_keys("sock")
	# 	searchBox.send_keys(Keys.RETURN)
	# 	result = driver.find_element_by_xpath("//div[@class='fashion-results']/div/div/div[@class='info anniversary women adult']/a")
	# 	self.assertTrue('sock' in result.text.lower())

	'''
	Navigate to the main page. Enter a combination of letters and numbers in the searh box.
	Once the search has been initiated, check to see that the URL has changed.
	Clear the search box and check special characters only. An alert should display since only
	special characters are not allowed.
	Clear the search box again and search for just numbers. This should open a URL that is
	different than the first one.
	'''
	# def testDifferentSearchInputs(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com")
	# 	searchBox = driver.find_element_by_id("keyword-search-input")

	# 	#Test numbers and letters
	# 	searchBox.send_keys("abc123")
	# 	searchBox.send_keys(Keys.RETURN)
	# 	self.assertNotEqual(driver.current_url, "http://shop.nordstrom.com")
	# 	pastURL = driver.current_url

	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.clear()

	# 	#Test just special characters
	# 	searchBox.send_keys("$%*(")
	# 	searchButton = driver.find_element_by_id("keyword-search-submit")
	# 	searchButton.click()

	# 	try:
	# 		WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Timed out')
	# 		alert = driver.switch_to.alert
	# 		alert.accept()
	# 	except TimeoutException:
	# 		self.fail("No alert is present")

	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.clear()	

	# 	#Test just numbers
	# 	searchBox.send_keys("765")
	# 	searchBox.send_keys(Keys.RETURN)
	# 	self.assertNotEqual(driver.current_url, pastURL)


	'''
	Navigate to main page. Enter gibberish text into searh box and use the 'Enter' key
	to search for it. Check to ensure that 'no results' are returned.
	'''
	# def testNotFound(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com")
	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.send_keys("aosentuhb")
	# 	searchBox.send_keys(Keys.RETURN)
	# 	result = driver.find_element_by_xpath("//div[@class='fashion-results']/h1")
	# 	self.assertTrue('no results' in result.text.lower())


	'''
	Navigate to the main page. Search for a specific product number of a suit.
	Ensure that the product page is directly displayed.
	'''
	# def testProductNumber(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com")
	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.send_keys("712826")
	# 	searchBox.send_keys(Keys.RETURN)
	# 	result = driver.find_element_by_xpath("//section[@id='product-title']/h1")
	# 	self.assertTrue('Milbank' in result.text)

	'''
	Navigate to the main page. Searh for 'sock.' Results should be returned.
	Click on the 'x' in the search box. No text should appear in search box.
	'''
	# def testClearButton(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com")
	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.send_keys("sock")
	# 	searchBox.send_keys(Keys.RETURN)

	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	clearButton = driver.find_element_by_id("keyword-search-reset")
	# 	clearButton.click()

	# 	self.assertEqual(searchBox.text, "")


	'''
	Navigate to main page. Check to see that entering 'jea' navigating away and
	then back, and using the arrow keys will move through the list of lookahead
	terms.
	'''
	# def testSearchLookahead(self):
	# 	driver = self.driver
	# 	driver.get("http://shop.nordstrom.com")
	# 	searchBox = driver.find_element_by_id("keyword-search-input")
	# 	searchBox.send_keys("jea")

	# 	driver.find_element_by_xpath("//body").click()
	# 	searchBox.click()

	# 	searchBox.send_keys(Keys.ARROW_DOWN)
	# 	searchBox.send_keys(Keys.ARROW_DOWN)

	# 	searchBox.send_keys(Keys.RETURN)
		
	# 	searchBox = driver.find_element_by_id("keyword-search-input")

	# 	self.assertTrue("keyword=jeans" in driver.current_url)






	def tearDown(self):
		# self.driver.quit()
		pass
		

if __name__ == "__main__":
	unittest.main()
