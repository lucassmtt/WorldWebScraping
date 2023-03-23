from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = Chrome()
browser.maximize_window()
browser.get('https://twitter.com/vagasprajr/with_replies')
html = browser.find_element(By.TAG_NAME, 'html')

for i in range(5):
    html.send_keys(Keys.ARROW_DOWN)