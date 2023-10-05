from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import datetime

driver = webdriver.Chrome()
driver.get('http://45.188.183.155:8079/transparencia/')

meses = {"1": "janeiro", "2": "fevereiro", "3": "março", "4": "abril", "5": "maio", "6": "junho", "7": "julho", "8": "agosto", "9": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"}

sleep(5)

arrecadacao_orcamentaria_geral = driver.find_element(By.XPATH, '//li[@id="LnkMenuReceitas"]/ul/li[@id="lnkReceitaOrcamentaria"]/a[@href="#"]')

# Usar o JavaScript para clicar, quando o elemento estiver coberto por outro elemento
driver.execute_script("arguments[0].click()", arrecadacao_orcamentaria_geral)

sleep(5)

# Acessar o Iframe:
driver.switch_to.frame('frmPaginaAspx')

sleep(1)

# Selecionar data inicial no calendário:
abri_calendario_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_B-1"]/table/tbody/tr/td').click()

sleep(2)

mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_TC"]/span').text.lower().strip()

while mes_inicial != 'janeiro de 2023':
    proximo_mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_NMC"]').click()
    mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_TC"]/span').text

localiza_dia_1 = driver.find_elements(By.XPATH, '//table[@id="datDataInicial_DDD_C_mt"]/tbody/tr[2]/td')

for td in localiza_dia_1:
    if td.text == '1':
        td.click()

sleep(5)

# Selecionar data final no calendário:
abri_calendario_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_B-1"]/table/tbody/tr/td').click()

sleep(5)

mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text.lower().strip()

# Pega a data atual, desconta um mês para pegar o mês anterior ao atual, converte o número do mês para o mês por extenso, e monte a string para ser utilizada na condição
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
mes_anterior = str(data_atual.month - 1)
mes_anterior_extenso = meses.get(mes_anterior)
mes_anterior_tratado = f'{mes_anterior_extenso} de {ano_atual}'

while mes_final != mes_anterior_tratado:
    # proximo_mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_NMC"]').click()
    mes_anterior_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_PMC"]').click()
    mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text

sleep(5)

localiza_dia_31 = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[6]/td')

for td in localiza_dia_31:
    if td.text == '30':
        td.click()
        print('CLICADAO')

print('pica')
sleep(20)




# data_inicial = driver.find_element(By.XPATH, '//input[@id="datDataInicial_I"]')

# Ir para a proxima pagina da tabela
# clica_proxima_pagina = driver.find_element(By.XPATH, '//table[@class="dxpControl"]/tbody/tr/td/table/tbody/tr/td[@class="dxpButton"]').click()

# sleep(5)

# valor_irrf = driver.find_element(By.XPATH, '//tr[@id="gridReceitas_DXDataRow36"]/td[8]').text

# print(valor_irrf)

# # Voltar para o contexto padrão
# driver.switch_to.default_content()

# sleep(20)

# driver.quit()