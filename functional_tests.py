from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_and_retrieve_list(self):
		
		# User visits the site.
		self.browser.get('http://localhost:8000')

		# User notices the title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# She is invited to enter a to-do item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types "Buy peacock feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates, and now it lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New item did not appear in table."
		)
		
		# There is still a text box to enter another item. She enters
		# "Use peacock feathers to make a fly".
		self.fail('Finish the test!')

		# The page updates again, and now shows both items on the list.
		
		# The site generates a unique url for this list, which will save the updates
		
		# User visits that url, and the list is still there.
		
		# Exit.

if __name__ == '__main__':
	unittest.main(warnings='ignore')
