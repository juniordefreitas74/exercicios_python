from datetime import datetime, timedelta, date,time

tamanhoCarro = 'g'
tempo_P = 30
tempo_M = 45
tempo_G = 5
data_atual = datetime.now()


if tamanhoCarro == 'p':
    data_estimada = data_atual + timedelta(minutes=(tempo_P))
    print(f'O carro chegou as: {data_atual}\ne ficará pronto as: {data_estimada}')

elif tamanhoCarro == 'm':
    
    data_estimada = data_atual + timedelta(minutes=(tempo_M))
    print(f'O carro chegou as: {data_atual} e ficará pronto as: {data_estimada}')


else:
    data_estimada = data_atual + timedelta(days=(tempo_G))
    print(f'O carro chegou as: {data_atual}\ne ficará pronto as: {data_estimada}')


print(date.today() - timedelta(days=2))
resultado = (datetime(2025,7,25,10,19,20) - timedelta(hours=1))#para ,manipular a hora ou data joga data/hora completa e faz a operação
print(resultado.time()) 
