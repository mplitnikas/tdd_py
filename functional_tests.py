from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

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

		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
		# There is still a text box to enter another item. She enters
		# "Use peacock feathers to make a fly".
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# The page updates again, and now shows both items on the list.
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		# The site generates a unique url for this list, which will save the updates
		self.fail('Finish the test.')

		# User visits that url, and the list is still there.
		
		# Exit.

if __name__ == '__main__':
	unittest.main(warnings='ignore')
