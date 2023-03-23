"""
Exercise Description:

1: Get all class links.
2: Get the exercise 3 link and enter.

LINK EXERCISE: https://selenium.dunossauro.live/aula_04.html
"""


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint


def search_elements():
    pass

my_browser = Chrome()
my_browser.get("https://selenium.dunossauro.live/aula_04.html")

sleep(1)

aside = my_browser.find_element(By.TAG_NAME, 'aside')

sleep(1)

link_in_aside = aside.find_elements(By.TAG_NAME, 'a')

sleep(1)

my_links_in_aside = dict()
for link in link_in_aside:

    """
    my_links_in_aside[link.text] = link.get_attribute("href")
    
    both are right
    """

    my_links_in_aside.setdefault(
        link.text,
        link.get_attribute("href")
    )

# for k, v in my_links_in_aside.items():
#     print(k, v)
# print('-'*30)
# pprint(my_links_in_aside)

main = my_browser.find_element(By.TAG_NAME, 'main')

link_in_main = main.find_elements(By.TAG_NAME, 'a')

exercise_links = {}
for i in link_in_main:
    exercise_links.setdefault(i.text, i.get_attribute("href"))

pprint(my_links_in_aside)
print('-'*60)
pprint(exercise_links)
