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
	Test to ensure that when the search button is pushed with an empty search box, a
	pop-up error is displayed.
	'''
	def testNoInputSearchPage(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com/sr?origin=keywordsearch&contextualcategoryid=0&keyword=")
		searchButton = driver.find_element_by_id("keyword-search-submit")
		searchButton.click()
		try:
			alert = driver.switch_to.alert
			a = alert.text
			self.assertEqual(a,"Please specify a search term.")
		except NoAlertPresentException:
			self.fail("No alert is present")


	'''
	Test to ensure that pressing the Return key initiates a search.
	'''
	def testSearchByEnter(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")
		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.send_keys("sock")
		searchBox.send_keys(Keys.RETURN)
		self.assertNotEqual(driver.current_url, "http://shop.nordstrom.com")


	'''
	Test to ensure that when searching for a word, results that display have that word
	in them.
	'''
	def testSearchSock(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")
		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.send_keys("sock")
		searchBox.send_keys(Keys.RETURN)
		result = driver.find_element_by_xpath("//div[@class='info anniversary women adult']/a")
		self.assertTrue('sock' in result.text.lower())

	'''
	Test different inputs to the search box. Numbers and letters should work.
	Special characters only should display an error pop-up.
	Just numbers should work.
	'''
	def testDifferentSearchInputs(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")
		searchBox = driver.find_element_by_id("keyword-search-input")

		#Test numbers and letters
		searchBox.send_keys("abc123")
		searchBox.send_keys(Keys.RETURN)
		self.assertNotEqual(driver.current_url, "http://shop.nordstrom.com")
		pastURL = driver.current_url

		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.clear()

		#Test just special characters
		searchBox.send_keys("$%*(")
		searchButton = driver.find_element_by_id("keyword-search-submit")
		searchButton.click()

		try:
			WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Timed out')
			alert = driver.switch_to.alert
			alert.accept()
		except TimeoutException:
			self.fail("No alert is present")

		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.clear()	

		#Test just numbers
		searchBox.send_keys("765")
		searchBox.send_keys(Keys.RETURN)
		self.assertNotEqual(driver.current_url, pastURL)


	'''
	Test to ensure that when a product is not found, the text 'no results' is displayed
	on the page
	'''
	def testNotFound(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")
		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.send_keys("aosentuhb")
		searchBox.send_keys(Keys.RETURN)
		result = driver.find_element_by_xpath("//div[@class='fashion-results']/h1")
		self.assertTrue('no results' in result.text.lower())


	'''
	Test to ensure that searching for a specific valid product number brings up the
	product page instead of search results.
	'''
	def testProductNumber(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")
		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.send_keys("712826")
		searchBox.send_keys(Keys.RETURN)
		result = driver.find_element_by_xpath("//section[@id='product-title']/h1")
		self.assertTrue('Milbank' in result.text)

	'''
	Test to ensure that when clicking the 'x' to clear the box, the box is actually cleared.
	'''
	def testClearButton(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")
		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.send_keys("sock")
		searchBox.send_keys(Keys.RETURN)


		clearButton = driver.find_element_by_id("keyword-search-reset")

		#Clear the box and ensure it is blank
		clearButton.click()
		searchBox = driver.find_element_by_id("keyword-search-input")
		self.assertEqual(searchBox.text, "")


	'''
	Test to ensure that when typing in a search term, a list of predictive
	terms are available to be chosen. When moving through the list and pressing
	Return, the search term in the list is searched for.
	'''
	def testSearchLookahead(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")
		searchBox = driver.find_element_by_id("keyword-search-input")
		searchBox.send_keys("jea")

		driver.find_element_by_xpath("//body").click()
		searchBox.click()

		searchBox.send_keys(Keys.ARROW_DOWN)
		searchBox.send_keys(Keys.ARROW_DOWN)

		searchBox.send_keys(Keys.RETURN)
		
		searchBox = driver.find_element_by_id("keyword-search-input")

		self.assertTrue("keyword=jeans" in driver.current_url)

	'''
	Test to ensure that the position of the search box is the same across multiple pages.
	'''
	def testSearchPositioning(self):
		driver = self.driver
		driver.get("http://shop.nordstrom.com")

		locationList = []

		searchElement = driver.find_element_by_id("keyword-search-input")
		location = searchElement.location
		locationList.append(location)

		driver.get("http://shop.nordstrom.com/c/shoes-shop?dept=8000001&origin=topnav")
		searchElement = driver.find_element_by_id("keyword-search-input")
		location = searchElement.location
		locationList.append(location)

		driver.get("http://shop.nordstrom.com/c/juniors-shop?dept=8000001&origin=topnav")
		searchElement = driver.find_element_by_id("keyword-search-input")
		location = searchElement.location
		locationList.append(location)				

		driver.get("http://shop.nordstrom.com/c/women?dept=8000001&origin=topnav")
		searchElement = driver.find_element_by_id("keyword-search-input")
		location = searchElement.location
		locationList.append(location)	

		same = True		
		for i in range(len(locationList)-1):
			if locationList[i]!=locationList[i+1]:
				same=False

		self.assertTrue(same)


	def tearDown(self):
		self.driver.quit()
		

if __name__ == "__main__":
	unittest.main(warnings='ignore', verbosity = 2)
