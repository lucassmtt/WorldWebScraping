from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from pprint import pprint


url = "https://selenium.dunossauro.live/aula_06_a.html"

my_browser = Chrome()
my_browser.get(url)

# my_search = my_browser.find_element(By.CSS_SELECTOR, "form")
# pprint(my_search.text)