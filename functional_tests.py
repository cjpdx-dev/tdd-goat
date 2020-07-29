from selenium import webdriver
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
		self.fail('Finish the test!')

		# Test 3
		# Test that a to-do item can be entered immediately

		# Test 4
		# Unit tests for to-do item

		# Test 5
		# After entering to-do item, test whether the page has
		# has updated successfully and is now displaying the to-do item.

		# Test 6
		# Repeat Test 5 on a second to-do item

		# Test 7
		# Test that the app remembers the list by generating a unique URL

		# Test 8
		# Test that visiting the URL brings back the old list state

		# browser.quit()

if __name__ == '__main__':
	unittest.main(warnings='ignore')

