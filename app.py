from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('http://45.188.183.155:8079/transparencia/')

# Acessar o Iframe:
# driver.switch_to.frame('frmPaginaAspx')

# tr_receitas = driver.find_element(By.ID, 'gridReceitas_DXDataRow36')

# # Voltar para o contexto padrão
# driver.switch_to.default_content()


# driver.quit()