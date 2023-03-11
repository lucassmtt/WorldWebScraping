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


def search_products(url: str, tag) -> [str]:
    my_links = {}
    browser = Chrome()

    browser.get(url)
    search = browser.find_elements(by.By.TAG_NAME, f'{tag}')

    for links in search:
        my_links.setdefault(f'{links.text}',
                            f'{links.get_attribute("href")}')

    return my_links


def search_collections(url: str, number: int, tag: str, options: str) -> [str]:
    """
    URL: search url
    TAG: search tag
    NUMBER: 1 == return link of collection
            2 == return search of products in links of collections
    OPTIONS: options of filters
    """

    browser = Chrome()

    browser.get(url)
    search = browser.find_elements(by.By.TAG_NAME, f'{tag}')

    for links in search:
        if links.text.lower() == options:
            links_collections = links.get_attribute('href')

            if number == 1:
                return links_collections
            else:
                return search_products(links_collections)



my_Search = search_products('https://templodela.com', 'a')

other_search = search_collections('https://templodela.com', '')