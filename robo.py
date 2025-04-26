from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='CAMINHO_DO_CHROMEDRIVER')
driver.get('https://web.whatsapp.com')

input("Escaneie o QR Code e pressione Enter...")

contato = "Nome do Contato"
mensagem = "Olá! Esta é uma mensagem automática."

# Localizar o contato e enviar mensagem
search_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(contato)
search_box.send_keys("\n")
sleep(2)

message_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="6"]')
message_box.send_keys(mensagem)
message_box.send_keys("\n")