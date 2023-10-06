import datetime

data_atual = datetime.datetime.now()
mes = data_atual.month


cont = 0

for mes in range(1, mes):
    print(f'mes: {mes}')
    cont += 1