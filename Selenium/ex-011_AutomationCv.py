from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = "SendingCV/local_driver"
driver = webdriver.Chrome(executable_path=chrome_path)
myPassword = ''
myEmail = ''
emailDest = ''


try:
    driver.get("https://www.gmail.com")

    # Preenchimento de campos de login
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys(f"{myEmail}")
    email_input.send_keys(Keys.RETURN)

    senha_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, f"{myPassword}"))
    )
    senha_input.send_keys("Ensfsn1230")
    senha_input.send_keys(Keys.RETURN)

    # Aguarda a página carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='COMPOR']"))
    )

    # Clicando em "Escrever"
    driver.find_element(By.XPATH, "//div[text()='COMPOR']").click()

    # Preenchendo destinatário, assunto e corpo do e-mail
    destinatario_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "to"))
    )
    destinatario_input.send_keys(f"{emailDest}")

    assunto_input = driver.find_element(By.NAME, "subjectbox")
    assunto_input.send_keys("Assunto do e-mail")

    corpo_input = driver.find_element(By.XPATH, "//div[@role='textbox']")
    corpo_input.send_keys("Corpo do e-mail")

    # Anexando arquivo
    anexar_botao = driver.find_element(By.XPATH, "//div[@command='Files']")
    anexar_botao.click()

    anexar_input = driver.find_element(By.XPATH, "//input[@type='file']")
    anexar_input.send_keys("/path/to/arquivo.pdf")

    # Enviando e-mail
    driver.find_element(By.XPATH, "//div[text()='Enviar']").click()

finally:
    driver.quit()


# import smtplib
# from email.mime.text import MIMEText

# # Configurações do e-mail
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# email = 'seuemail@gmail.com'
# password = 'suasenha'
# destinatario = 'destinatario@example.com'

# # Cria o objeto MIMEText com o conteúdo do e-mail
# conteudo = 'Olá, este é um e-mail enviado por Python!'
# mensagem = MIMEText(conteudo)

# # Configura os campos "De", "Para" e "Assunto" da mensagem
# mensagem['From'] = email
# mensagem['To'] = destinatario
# mensagem['Subject'] = 'E-mail enviado por Python'

# # Conecta-se ao servidor SMTP e envia a mensagem
# smtp = smtplib.SMTP(smtp_server, smtp_port)
# smtp.starttls()
# smtp.login(email, password)
# smtp.sendmail(email, destinatario, mensagem.as_string())
# smtp.quit()