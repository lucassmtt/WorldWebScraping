from selenium.webdriver import Chrome
from selenium.webdriver.common import by


# my_browser = Chrome()
# my_browser.get('https://templodela.com')
#
# search = my_browser.find_element(by.By.TAG_NAME, 'ul') #pega somente a primeira
#                                                        #aparição do ul
# print(search.text)
# print('-'*30)
#
# other_search = my_browser.find_elements(by.By.TAG_NAME, 'a')#pega todas as aparições
# for items in other_search:
#     print(items.get_attribute('href'))


def search_products(url: str) -> [str]:
    my_links = list()
    browser = Chrome()

    browser.get(url)
    search = browser.find_elements(by.By.TAG_NAME, 'a')

    for links in search:
        my_links.append(links.get_attribute('href'))

    return my_links

print(search_products('https://templodela.com'))

