lista = [1, 'junior', 32, [35, 78, 16]]

copia_lista = lista.copy()  # copia todos os elementos da lista para copia_lista

print(lista)
print(copia_lista)
print('********************************************')

copia_lista[1] = 'Lara de Freitas'
print(lista)
print(copia_lista)

print('********************************************')
print('********************************************')

cores = ['azul', 'verde', ' amarelo', 'verde', 'verde', 'azul', 'roxo']

# conta a quantidade que a palavra azul aparece na lista
print(cores.count('azul'))
print(cores.count('verde'))
print(cores.count('roxo'))
print(cores.count('amarelo'))
print(f'a qtd de azul é: {cores.count('azul')}')

print('\n********************************************\n')


cores.reverse()  # inverte a lista
print(cores)

print('\n********************************************\n')

cores.remove('roxo')  # remove roxo da lista
print(cores)
print('\n********************************************\n')

cores.pop()  # remove ultimo item da lista
print(cores)
cores.pop(0)  # remove primeiro item da lista
print(cores)

print('\n********************************************\n')
cores2 = ['azul', 'verde', ' amarelo', 'verde', 'verde', 'azul', 'roxo']

cores.extend(['rato', 'sapato'])  # adiciona uma lista dentro de outra lista
print(cores)
cores.extend(cores2)  # adiciona uma lista dentro de outra lista
print(cores)

print('\n********************************************\n')
cores23 = ['eu', 'azul', 'verde', 'amarelo', 'verde', 'verde', 'azul', 'roxo']
cores23.sort()  # ordena a lista em ordem alfabética
print(cores23)

cores23.sort(reverse=True)  # ordena e inverte a lista em ordem alfabética
print(cores23)

# ordena e inverte a lista em ordem alfabética
cores23.sort(key=lambda x: len(x))
print(cores23)

print('\n********************************************\n')
texto = 'quintino Junior'
print(len(cores23))  # retorna a quantidade de itens que tem na lista
print(len(texto))  # retorna a quantidade de letras que a string contem

print('\n********************************************\n')
cores24 = ['eu', 'azul', 'verde', 'amarelo', 'verde', 'verde', 'azul', 'roxo']

print(sorted(cores24))  # retorna a lista em ordem alfabetica
