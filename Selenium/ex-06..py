from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

browser = Chrome()
browser.get('http://selenium.dunussauro.live/aula_04_b.html')
browser.find_element(By.TAG_NAME, '')