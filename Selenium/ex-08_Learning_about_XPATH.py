from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint


"""
/html/title : Traz a primeira ocorrência seguindo a árvore
//title : Traz a primeira ocorrências ignorando a árvore
ul/* : Traz qualquer tag que vier abaixo
ul//* : Vai retornar todas as tags que vier abaixo, inclusive aninhadas
(ul//*)[2] : Vai pegar a expressão inteira e selecionar a segunda ocorrência

"""


url = 'https://rennerocha.github.io/xpath/'
browser = Chrome()
browser.get(url)
sleep(2)
element = browser.find_element(By.XPATH, "/html")
pprint(element.text)