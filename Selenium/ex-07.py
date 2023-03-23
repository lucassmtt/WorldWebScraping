"""
Exercise Description:

1: Get all class links.
2: Get the exercise 3 link and enter.

LINK EXERCISE: https://selenium.dunossauro.live/aula_04.html
"""

from selenium.webdriver import Chrome
from pprint import pprint


def get_links(browser, element, url) -> [dict]:
    """
    Get links by select element

    Browser: Your favorite browser
    Element: Your select element
    Url: Your select url for Web Scraping

    """
    from selenium.webdriver.common.by import By
    from time import sleep


    my_browser = browser()
    my_browser.get(url)
    sleep(1)

    element = my_browser.find_element(By.TAG_NAME, f'{element}')
    sleep(1)

    link_in_element = element.find_elements(By.TAG_NAME, 'a')
    sleep(1)

    my_links_in_web_element = dict()
    for link in link_in_element:
        my_links_in_web_element.setdefault(
            link.text,
            link.get_attribute("href")
        )

    return my_links_in_web_element


exercise_01 = get_links(
    browser=Chrome,
    element='aside',
    url='https://selenium.dunossauro.live/aula_04.html'
)
pprint(exercise_01)

print('-'*40)

exercise_02 = get_links(
    browser=Chrome,
    element='main',
    url='https://selenium.dunossauro.live/aula_04.html'
)
pprint(exercise_02)