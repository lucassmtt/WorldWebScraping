from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

chrome = Chrome()
chrome.get('https://github.com/lucassmtt')

my_search = chrome.find_element(By.TAG_NAME, 'div')
for item in my_search.text:
    if item == 'System_with_PyQt6':
        my_search.click()

print(my_search.text)

