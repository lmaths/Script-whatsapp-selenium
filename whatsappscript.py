from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('INFORME O NOME DO GRUPO OU DO USUARIO : ')
msg = input('INSIRA SUA MENSAGEM : ')
count = int(input('DESEJA ENVIAR QUANTAS VEZES?: '))

input('APERTE ALGO APÓS LER O CODIGO QR NO NAVEGADOR')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
button.click()