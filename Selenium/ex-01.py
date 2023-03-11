from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
"""
OBS: é importante lembrar que em versões mais recentes do Selenium
temos que importar o "By" 
"""

chrome = Chrome()
chrome.get('https://github.com/lucassmtt')#busca a url

my_search = chrome.find_elements(By.TAG_NAME, 'div')#faz uma pesquisa usando
                                                    #o By(por nome de tag)

for i in my_search: #looping na minha pesquisa
    print(i.text)

