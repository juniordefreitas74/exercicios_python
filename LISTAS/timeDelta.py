from datetime import datetime, timedelta

tamanhoCarro = 'g'
tempo_P = 30
tempo_M = 45
tempo_G = 60
data_atual = datetime.now()


if tamanhoCarro == 'p':
    # o time delta vc escolhe o que vc quer somar ou subtrair, neste caso minutos
    data_estimada = data_atual + timedelta(minutes=tempo_P)
    print(data_atual)
    print(data_estimada)
    print(
        f'O carro chegou as: {data_atual} e fiacará pronto as{data_estimada}')

if tamanhoCarro == 'm':
    data_estimada = data_atual + timedelta(minutes=tempo_M)
    print(data_atual)
    print(data_estimada)
    print(
        f'O carro chegou as: {data_atual} e fiacará pronto as{data_estimada}')

if tamanhoCarro == 'g':
    data_estimada = data_atual + timedelta(minutes=tempo_G)
    print(data_atual)
    print(data_estimada)
    print(
        f'O carro chegou as: {data_atual} e fiacará pronto as{data_estimada}')
