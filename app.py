from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('http://45.188.183.155:8079/transparencia/')

sleep(10)
arrecadacao_orcamentaria_geral = driver.find_element(By.XPATH, '//li[@id="LnkMenuReceitas"]/ul/li[@id="lnkReceitaOrcamentaria"]/a[@href="#"]')

# Usar o JavaScript quando o elemento estiver coberto por outro elemento
driver.execute_script("arguments[0].click()", arrecadacao_orcamentaria_geral)

sleep(15)
# print(li_receitas)
# Acessar o Iframe:
# driver.switch_to.frame('frmPaginaAspx')




# irrf = driver.find_element(By.XPATH, '//tr[@id="gridReceitas_DXDataRow36"]')

# irr_texto = irrf.text



# Voltar para o contexto padrão
# driver.switch_to.default_content()


# driver.quit()