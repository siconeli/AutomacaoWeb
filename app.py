from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('http://45.188.183.155:8079/transparencia/')

sleep(5)

arrecadacao_orcamentaria_geral = driver.find_element(By.XPATH, '//li[@id="LnkMenuReceitas"]/ul/li[@id="lnkReceitaOrcamentaria"]/a[@href="#"]')

# Usar o JavaScript para clicar, quando o elemento estiver coberto por outro elemento
driver.execute_script("arguments[0].click()", arrecadacao_orcamentaria_geral)

sleep(5)

# Acessar o Iframe:
driver.switch_to.frame('frmPaginaAspx')

sleep(5)

data_inicial = driver.find_element(By.XPATH, '//input[@id="datDataInicial_I"]').send_keys('01/09/2023')

sleep(5)

# Ir para a proxima pagina da tabela
clica_proxima_pagina = driver.find_element(By.XPATH, '//table[@class="dxpControl"]/tbody/tr/td/table/tbody/tr/td[@class="dxpButton"]').click()

sleep(5)

valor_irrf = driver.find_element(By.XPATH, '//tr[@id="gridReceitas_DXDataRow36"]/td[8]').text

print(valor_irrf)

# Voltar para o contexto padrão
driver.switch_to.default_content()

sleep(20)





# driver.quit()