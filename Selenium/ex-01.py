from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

chrome = Chrome()
chrome.get('https://github.com/lucassmtt')

my_search = chrome.find_elements(By.TAG_NAME, 'div')

for i in my_search:
    print(i.text)

