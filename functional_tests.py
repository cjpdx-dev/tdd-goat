from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	# uncomment when we get tired of opening firefox windows
	# def tearDown(self):
		# self.browser.quit()

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
		inputbox.send_keys('1. Test entry.')

		# Test 5
		# After entering to-do item, test whether the page has
		# has updated successfully and is now displaying the to-do item.
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_elements_by_tag_name('tr')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Test entry.' for row in rows)
		)

		# Test 6
		# Repeat Test 5 on a second to-do item
		self.fail('Finish the test (Test 6)')
		# Test 7
		# Test that the app remembers the list by generating a unique URL

		# Test 8
		# Test that visiting the URL brings back the old list state

		# browser.quit()

if __name__ == '__main__':
	unittest.main(warnings='ignore')

