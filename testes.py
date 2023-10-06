import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import datetime

driver = webdriver.Chrome()
driver.get('http://45.188.183.155:8079/transparencia/')
print('Realizei o carregamento do site')

meses_conversao = {"1": "janeiro", "2": "fevereiro", "3": "março", "4": "abril", "5": "maio", "6": "junho", "7": "julho", "8": "agosto", "9": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"}


meses_calendario = ["janeiro de 2023", "fevereiro de 2023", "março de 2023", "abril de 2023", "maio de 2023", "junho de 2023", "julho de 2023", "agosto de 2023", "setembro de 2023", "outubro de 2023", "novembro de 2023", "dezembro de 2023"]

sleep(5)

arrecadacao_orcamentaria_geral = driver.find_element(By.XPATH, '//li[@id="LnkMenuReceitas"]/ul/li[@id="lnkReceitaOrcamentaria"]/a[@href="#"]')

# Usar o JavaScript para clicar, quando o elemento estiver coberto por outro elemento
driver.execute_script("arguments[0].click()", arrecadacao_orcamentaria_geral)
print('Cliquei no menu "Arrecadação Orçamentaria - Geral"')

sleep(5)

# Acessar o Iframe:
driver.switch_to.frame('frmPaginaAspx')
print('Acessei o Iframe')
print('\n')

sleep(1)

# Selecionar data inicial no calendário:
abri_calendario_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_B-1"]/table/tbody/tr/td').click()
print('Abri o calendário Data Inicial')

sleep(2)

mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_TC"]/span').text.lower().strip()

for mes in meses_calendario:
    # Se o mês for igual a janeiro:
    if mes == mes_inicial:
        localiza_dia_1 = driver.find_elements(By.XPATH, '//table[@id="datDataInicial_DDD_C_mt"]/tbody/tr[2]/td')
        for dia in localiza_dia_1:
            if dia.text == '1':
                dia.click()
                print(f'Selecionei o dia e mês inicial: 01 de {mes}')
                sleep(5)

        abri_calendario_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_B-1"]/table/tbody/tr/td').click()
        print('Abri o calendário Data Final')

        mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text.lower().strip()
        
        sleep(2)

        while mes_final != mes:
            mes_anterior_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_PMC"]').click()
            mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text
        print(f'Igualei o mês final com o mês inicial: {mes}')

        localiza_ultimo_dia = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[6]/td')

        ultimos_dias_inicial = []

        for dia in localiza_ultimo_dia:
            dia_texto = dia.text
            dia_inteiro = int(dia_texto)
            ultimos_dias_inicial.append(dia_inteiro)

        ultimo_dia = str(max(ultimos_dias_inicial))
        
        for dia in localiza_ultimo_dia:
            if dia.text == ultimo_dia:
                dia.click()   
                print(f'Selecionei o último dia do mês do calendário de Data Final: Dia {ultimo_dia}')
        
        # Inserir o código para pegar os dados da tabela e inserir no excel...

        print(f'Fim do mês: {mes}')
        print('\n')
        sleep(5)
    
        print('Próximo mês!')
        print('\n')
        abri_calendario_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_B-1"]/table/tbody/tr/td').click()
        print('Abri o calendário Data Inicial')
        sleep(5)

    # Se o mês for diferente de janeiro: 
    if mes != mes_inicial:
        while mes_inicial != mes:
            proximo_mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_NMC"]').click()
            mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_TC"]/span').text.lower().strip()
            sleep(5)

            localiza_dia_1 = driver.find_elements(By.XPATH, '//table[@id="datDataInicial_DDD_C_mt"]/tbody/tr[2]/td')
            for dia in localiza_dia_1:
                if dia.text == '1':
                    dia.click()
                    print(f'Selecionei o dia e mês inicial: 01 de {mes}')
                    sleep(5)

            abri_calendario_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_B-1"]/table/tbody/tr/td').click()
            print('Abri o calendário Data Final')

            mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text.lower().strip()
        
            sleep(2)

            while mes_final != mes_inicial:
                proximo_mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_NMC"]').click()
                mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text
                print(f'Igualei o mês final com o mês inicial: {mes}')

            localiza_ultimo_dia = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[6]/td')

            ultimos_dias_final = []

            for dia in localiza_ultimo_dia:
                dia_texto = dia.text
                dia_inteiro = int(dia_texto)
                ultimos_dias_final.append(dia_inteiro)

            ultimo_dia = str(max(ultimos_dias_final))
            
            for dia in localiza_ultimo_dia:
                if dia.text == ultimo_dia:
                    dia.click()   
                    print(f'Selecionei o último dia do mês do calendário de Data Final: Dia {ultimo_dia}')

        print(f'Fim do mês: {mes}')
        print('\n')
        sleep(5)

        abri_calendario_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_B-1"]/table/tbody/tr/td').click()
        print('Abri o calendário Data Inicial')
        sleep(5)

        # Pega a data atual, desconta um mês para pegar o mês anterior ao atual, converte o número do mês para o mês por extenso, e monte a string para ser utilizada na condição
        data_atual = datetime.datetime.now()
        ano_atual = data_atual.year
        mes_anterior = str(data_atual.month)
        mes_anterior_extenso = meses_conversao.get(mes_anterior)
        mes_anterior_tratado = f'{mes_anterior_extenso} de {ano_atual}'

        if mes_inicial == mes_anterior_tratado:
            break

        sleep(5)


 
sleep(150)






