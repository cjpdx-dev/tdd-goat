from selenium import webdriver

browser = webdriver.Firefox()


# Test that homepage exists 
browser.get('http://localhost:8000')

# Test that the page title and header are accurate
assert 'Django' in browser.title 

# Test that a to-do item can be entered immediately


