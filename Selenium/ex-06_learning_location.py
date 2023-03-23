from selenium.webdriver import Chrome
from selenium.webdriver.common import by
from urllib.parse import urlparse


my_browser = Chrome()
my_browser.get("https://google.com")

url_parsed = urlparse(my_browser.current_url)
