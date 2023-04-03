from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from pprint import pprint


url = "https://selenium.dunossauro.live/aula_06_a.html"

my_browser = Chrome()
my_browser.get(url)

# my_search = my_browser.find_element(By.CSS_SELECTOR, "form")
# pprint(my_search.text)

pesquisa = my_browser.find_elements(By.CSS_SELECTOR, "[for]")

"""
[atributo =  valor] : Deve ser exatamente igual
[atributo *= valor] : Deve ocorrer em
[atributo |= valor] : Deve ser exatamente ou iniciar
[atributo ^= valor] : Iniciado em
[atributo $= valor] : Terminado em
[atributo ~= valor] : Um deve ser exatamente igual
"""

pesquisa_1 = my_browser.find_elements(
    By.CSS_SELECTOR, "[class='form-group']"
)# Todos atributos CLASS em que o valor seja exatamente igual a FORM-GROUP

pesquisa_2 = my_browser.find_elements(
    By.CSS_SELECTOR, "[class*='group']"
)# Todos atributos CLASS em que a palavra GROUP exista

pesquisa_3 = my_browser.find_elements(
    By.CSS_SELECTOR, "[class|='no']"
)# Deve ser exatamente ou iniciar com "no" -> nome

pesquisa_4 = my_browser.find_elements(
    By.CSS_SELECTOR, "[class^='fo']"
)# Deve ser iniciada com "fo" -> form

pesquisa_5 = my_browser.find_elements(
    By.CSS_SELECTOR, "[type$='t']"
)# Todos atributos type que terminam com a letra "t"

pesquisa_6 = my_browser.find_elements(
    By.CSS_SELECTOR, "[~=]"
)# Um deve ser exatamente igual


