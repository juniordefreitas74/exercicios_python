frutas1 = ['laranja', 'banana', 'uva', 'pera', 'jaca']
print(frutas1)  # lista simples

frutas2 = []  # lista vazia
print(frutas2)

letras = list('python')  # transforma cada letra da palavra em um ítem da lista
print(letras)

numeros = list(range(11))  # faz uma lista com numeros de 0 a 10
print(numeros)

carro = ['Ferrari', 'F8', 420000.00, 2025, 2900, 'São Paulo', True]
print(carro)  # lista mista de numeros , strings e booleanos

# a lista é uma sequencia que começa do indice 0 em diante
print(frutas1[0])  # imprime o primeiro item da lista
print(frutas1[-1])  # imprime o último item da lista
print('======================================================')
matriz = [
    [1, 'a', '2', 9],  # dessa forma eu tenho uma tabela
    ['b', 3, 4, 'd'],  # de 3 linhas e 4 colunas
    [6, 5, 'c', 'e']
]
print(matriz[0])  # print primeira linha
print(matriz[0][0])  # print item da  primeira linha e da primeira coluna
print(matriz[0][-1])  # print o ultimo item da primeira  linha
print(matriz[-1][-1])  # print o ultimo item da última  linha

print('======================================================')
# FATIAMENTO (  pegar pedaços de listas)

teste_fatiamento = ['p', 'y', 't', 'h', 'o', 'n']
print(teste_fatiamento[2:])  # pega a apartir do segundo até o final
print(teste_fatiamento[:2])  # pega do segundo pra trás
# pega do segundo até o terceiro (le pega -1) ou seja 1 antes do numero colocado
print(teste_fatiamento[1:3])
# pega do primeiro até o terceiro pulando de 2 casas
print(teste_fatiamento[0:3:2])
print(teste_fatiamento[::-1])  # pega a lista inteira invertida

print('======================================================')

print('======================================================')

carros = ['gol', 'fiesta', 'uno', 'fox']

for concessionaria in carros:  # colque dentro de concessionaria o que tem dentro de carros
    print(concessionaria)

print('======================================================')

print('======================================================')

carros2 = ['gol', 'fiesta', 'uno', 'fox']

# colque dentro de concessionaria o que tem dentro de carros
# coloca um ince enumerando a posição de cada item
for indice, concessionaria in enumerate(carros2):
    print(f'{indice} - {concessionaria}')

print('======================================================')

print('======================================================')

numeral = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []

for resultado in numeral:  # coloque em resultado todos os itens de numeral
    if resultado % 2 == 0:  # se a divisão por 2 de cada iten de'resultado' for exatamente  igual a 0
        # insira esse numero (da lista resultado) na lista numeros_pares
        numeros_pares.append(resultado)
print(numeros_pares)

print('======================================================')

print('======================================================')
# compressão codigo em 1 linha
numeral2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares2 = [resultado2 for resultado2 in numeral2 if resultado2 % 2 == 0]
print(numeros_pares2)

print('======================================================')

print('======================================================')


numeral = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []

for resultado in numeral:  # coloque em resultado todos os itens de numeral
    # insira esse numero (da lista resultado) na lista numeros_pares elevando ao quadrado
    numeros_pares.append(resultado**2)
print(numeros_pares)
