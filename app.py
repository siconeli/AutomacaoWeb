import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import datetime

driver = webdriver.Chrome()
driver.get('http://45.188.183.155:8079/transparencia/')
print('-> Carregamento de site realizado:')

meses_calendario = ["janeiro de 2023", "fevereiro de 2023", "março de 2023", "abril de 2023", "maio de 2023", "junho de 2023", "julho de 2023", "agosto de 2023", "setembro de 2023", "outubro de 2023", "novembro de 2023", "dezembro de 2023"]

meses_conversao = {"1": "janeiro", "2": "fevereiro", "3": "março", "4": "abril", "5": "maio", "6": "junho", "7": "julho", "8": "agosto", "9": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"}

sleep(5)

arrecadacao_orcamentaria_geral = driver.find_element(By.XPATH, '//li[@id="LnkMenuReceitas"]/ul/li[@id="lnkReceitaOrcamentaria"]/a[@href="#"]')

# Usar o JavaScript para clicar, quando o elemento estiver coberto por outro elemento
driver.execute_script("arguments[0].click()", arrecadacao_orcamentaria_geral)
print('-> Abrindo "Arrecadação Orçamentaria - Geral"')

sleep(5)

# Acessar o Iframe:
driver.switch_to.frame('frmPaginaAspx')
print('\n')

sleep(1)

# Selecionar data inicial no calendário:
abri_calendario_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_B-1"]/table/tbody/tr/td').click()
print('-> Abrindo calendário data inicial:')

sleep(2)

valores_receita = []

mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_TC"]/span').text.lower().strip()

print(f'-> Início do mês {mes_inicial}')

for mes in meses_calendario:
    # Se o mês for igual a janeiro:
    if mes == mes_inicial:
        localiza_dia_1 = driver.find_elements(By.XPATH, '//table[@id="datDataInicial_DDD_C_mt"]/tbody/tr[2]/td')
        for dia in localiza_dia_1:
            if dia.text == '1':
                dia.click()
                print(f'-> Dia e mês inicial selecionado: 01 de {mes}')
                sleep(2)

        abri_calendario_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_B-1"]/table/tbody/tr/td').click()
        print('-> Abrindo calendário data final')

        mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text.lower().strip()
    
        sleep(2)

        while mes_final != mes_inicial:
            proximo_mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_NMC"]').click()
            mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text
            print(f'-> Igualando o mês final com o mês inicial')

        maiores = []

        localiza_ultimo_dia_linha_4 = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[5]/td[@class="dxeCalendarDay_DevEx"]')

        if localiza_ultimo_dia_linha_4:
            lista_dias_linha_4 = []

            for dia in localiza_ultimo_dia_linha_4:
                dia_texto = dia.text
                dia_inteiro = int(dia_texto)
                lista_dias_linha_4.append(dia_inteiro)

            maiores.append(max(lista_dias_linha_4))

        localiza_ultimo_dia_linha_5 = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[6]/td[@class="dxeCalendarDay_DevEx"]')
        
        if localiza_ultimo_dia_linha_5:
            lista_dias_linha_5 = []

            for dia in localiza_ultimo_dia_linha_5:
                dia_texto = dia.text
                dia_inteiro = int(dia_texto)
                lista_dias_linha_5.append(dia_inteiro)

            maiores.append(max(lista_dias_linha_5))

        localiza_ultimo_dia_linha_6 = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[7]/td[@class="dxeCalendarDay_DevEx"]')

        if localiza_ultimo_dia_linha_6:
            lista_dias_linha_6 = []

            for dia in localiza_ultimo_dia_linha_6:
                dia_texto = dia.text
                dia_inteiro = int(dia_texto)
                lista_dias_linha_6.append(dia_inteiro)

            maiores.append(max(lista_dias_linha_6))

        ultimo_dia = str(max(maiores))
        
        for dia in localiza_ultimo_dia_linha_4:
            if dia.text == ultimo_dia:
                dia.click()   
                print(f'-> Selecionando o último dia do mês: {ultimo_dia}')
                sleep(5)

        for dia in localiza_ultimo_dia_linha_5:
            if dia.text == ultimo_dia:
                dia.click()   
                print(f'-> Selecionando o último dia do mês: {ultimo_dia}')
                sleep(5)

        for dia in localiza_ultimo_dia_linha_6:
            if dia.text == ultimo_dia:
                dia.click()   
                print(f'-> Selecionando o último dia do mês: {ultimo_dia}')
                sleep(5)
        
        # Ir para a proxima pagina da tabela
        clica_proxima_pagina = driver.find_element(By.XPATH, '//table[@class="dxpControl"]/tbody/tr/td/table/tbody/tr/td[@class="dxpButton"]').click()
        print('-> Próxima página')

        sleep(2)

        valor_irrf = driver.find_element(By.XPATH, '//tr[@id="gridReceitas_DXDataRow36"]/td[8]').text

        valores_receita.append(valor_irrf)

        print(f'-> Valor R${valor_irrf} salvo na lista')
        
        print(f'-> Fim do mês: {mes}')
        print('\n')
        sleep(2)
    
        print('-> Próximo mês!')
        print('\n')
        abri_calendario_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_B-1"]/table/tbody/tr/td').click()
        print('-> Abrindo calendário data inicial:')
        sleep(2)

    # Se o mês for diferente de janeiro: 
    if mes != mes_inicial:
        while mes_inicial != mes:
            proximo_mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_NMC"]').click()
            mes_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_DDD_C_TC"]/span').text.lower().strip()
            sleep(2)

            localiza_dia_1 = driver.find_elements(By.XPATH, '//table[@id="datDataInicial_DDD_C_mt"]/tbody/tr[2]/td')
            for dia in localiza_dia_1:
                if dia.text == '1':
                    dia.click()
                    print(f'-> Dia e mês inicial selecionado: 01 de {mes}')
                    sleep(5)

            abri_calendario_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_B-1"]/table/tbody/tr/td').click()
            print('-> Abrindo calendário data final')

            mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text.lower().strip()
        
            sleep(2)

            while mes_final != mes_inicial:
                proximo_mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_NMC"]').click()
                mes_final = driver.find_element(By.XPATH, '//td[@id="datDataFinal_DDD_C_TC"]/span').text
                print(f'-> Igualando o mês final com o mês inicial')

            maiores = []

            localiza_ultimo_dia_linha_4 = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[5]/td[@class="dxeCalendarDay_DevEx"]')

            if localiza_ultimo_dia_linha_4:
                lista_dias_linha_4 = []

                for dia in localiza_ultimo_dia_linha_4:
                    dia_texto = dia.text
                    dia_inteiro = int(dia_texto)
                    lista_dias_linha_4.append(dia_inteiro)

                maiores.append(max(lista_dias_linha_4))

            localiza_ultimo_dia_linha_5 = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[6]/td[@class="dxeCalendarDay_DevEx"]')
            
            if localiza_ultimo_dia_linha_5:
                lista_dias_linha_5 = []

                for dia in localiza_ultimo_dia_linha_5:
                    dia_texto = dia.text
                    dia_inteiro = int(dia_texto)
                    lista_dias_linha_5.append(dia_inteiro)

                maiores.append(max(lista_dias_linha_5))

            localiza_ultimo_dia_linha_6 = driver.find_elements(By.XPATH, '//table[@id="datDataFinal_DDD_C_mt"]/tbody/tr[7]/td[@class="dxeCalendarDay_DevEx"]')

            if localiza_ultimo_dia_linha_6:
                lista_dias_linha_6 = []

                for dia in localiza_ultimo_dia_linha_6:
                    dia_texto = dia.text
                    dia_inteiro = int(dia_texto)
                    lista_dias_linha_6.append(dia_inteiro)

                maiores.append(max(lista_dias_linha_6))

            ultimo_dia = str(max(maiores))
            
            for dia in localiza_ultimo_dia_linha_4:
                if dia.text == ultimo_dia:
                    dia.click()   
                    print(f'-> Selecionando o último dia do mês: {ultimo_dia}')

            for dia in localiza_ultimo_dia_linha_5:
                if dia.text == ultimo_dia:
                    dia.click()   
                    print(f'-> Selecionando o último dia do mês: {ultimo_dia}')

            for dia in localiza_ultimo_dia_linha_6:
                if dia.text == ultimo_dia:
                    dia.click()   
                    print(f'-> Selecionando o último dia do mês: {ultimo_dia}')

            # Ir para a proxima pagina da tabela
            clica_proxima_pagina = driver.find_element(By.XPATH, '//table[@class="dxpControl"]/tbody/tr/td/table/tbody/tr/td[@class="dxpButton"]').click()
            print('-> Próxima página')

            sleep(2)

            valor_irrf = driver.find_element(By.XPATH, '//tr[@id="gridReceitas_DXDataRow36"]/td[8]').text

            valores_receita.append(valor_irrf)

            print(f'-> Valor R${valor_irrf} salvo na lista')

        print(f'-> Fim do mês: {mes}')
        print('\n')
        sleep(5)

        abri_calendario_inicial = driver.find_element(By.XPATH, '//td[@id="datDataInicial_B-1"]/table/tbody/tr/td').click()
        print('-> Abrindo calendário data')
        sleep(5)

        # Pega a data atual, desconta um mês para pegar o mês anterior ao atual, converte o número do mês para o mês por extenso, e monta a string para ser utilizada na condição
        data_atual = datetime.datetime.now()
        ano_atual = data_atual.year
        mes_anterior = data_atual.month -1
        mes_anterior = str(mes_anterior)
        mes_anterior_extenso = meses_conversao.get(mes_anterior)
        mes_anterior_tratado = f'{mes_anterior_extenso} de {ano_atual}'

        if mes_inicial == mes_anterior_tratado:
            print(f'-> O mês {mes_anterior_tratado} é 1 mês anterior ao mês atual, finalizando automação...')

            print(f'-> Lista de valores IRRF mês a mês: {valor_irrf}')

            driver.quit()


    







