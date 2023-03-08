from selenium.webdriver import Chrome
from selenium.webdriver.common import by
my_browser = Chrome()
my_browser.get('https://selenium.dunossauro.live/aula_04_a.html')

search = my_browser.find_element(by.By.TAG_NAME, 'ul') #pega somente a primeira
                                                       #aparição do ul
print(search.text)
print('-'*30)

other_search = my_browser.find_elements(by.By.TAG_NAME, 'ul')#pega todas as aparições
for items in other_search:
    print(items.text)

