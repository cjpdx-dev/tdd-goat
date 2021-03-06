from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	# uncomment when we get tired of opening firefox windows
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):

		# Test 1
		# Test that homepage exists 
		self.browser.get('http://localhost:8000')

		# Test 2
		# Test that the page title and header are accurate
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# Test 3
		# Test that a to-do item can be entered immediately
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# Test 4
		# Test an entry into the text box
		inputbox.send_keys('Buy peacock feathers')

		# Test 5
		# After entering to-do item, test whether the page has
		# has updated successfully and is now displaying the to-do item.
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
		# Test 6
		# Repeat Test 5 on a second to-do item and test if both items are remembered
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# Test 7
		# Test that the app remembers the list by generating a unique URL
		self.fail('Finish the test (Test 6)')
		# Test 8
		# Test that visiting the URL brings back the old list state

		# browser.quit()

if __name__ == '__main__':
	unittest.main(warnings='ignore')

