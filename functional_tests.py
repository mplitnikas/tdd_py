from selenium import webdriver
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
		self.fail('finish the test!')
		
		# She is invited to enter a to-do item right away
		
		# She types "buy peacock feathers" into a text box
		
		# When she hits enter, the page updates, and now it lists
		# "1: Buy peacock feathers" as an item in a to-do list
		
		# There is still a text box to enter another item. She enters
		# "Use peacock feathers to make a fly".
		
		# The page updates again, and now shows both items on the list.
		
		# The site generates a unique url for this list, which will save the updates
		
		# User visits that url, and the list is still there.
		
		# Exit.

if __name__ == '__main__':
	unittest.main(warnings='ignore')
	