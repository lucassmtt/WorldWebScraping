from selenium.webdriver import Chrome
from selenium.webdriver.common import by


def search_link_in_site(url: str, tag_name: str, text: str) -> [str] or None:
    link_nested = {}
    browser = Chrome()

    browser.get(url)
    search = browser.find_elements(by.By.TAG_NAME, tag_name)

    for link in search:
        if link.text == f'{text}':
            browser.get(f'{link.get_attribute("href")}')

            search_nested = browser.find_elements(by.By.TAG_NAME, tag_name)
            for link_search_nested in search_nested:
                link_nested.setdefault(f'{link_search_nested.text}',
                                       link_search_nested.get_attribute("href"))
            return link_nested

    return link_nested


my_search = search_link_in_site('https://templodela.com', 'a', 'VER TUDO')
print(my_search)