'''
Conjuntos são declarados dentro de chaves{}
'''

# o SET elimina itens repetidos

numeros = (set([2, 6, 1, 5, 2, 3, 4, 1, 2, 6, 1, 5, 2, 3, 4, 1]))

print(numeros)
fruta = (set('abacaxi'))
print(fruta)
print('\n=======================\n')
carros = set(('palio', 'gol', 'uno', 'uno'))
print(carros)
print('\n=======================\n')
# outra forma de clarar um set para eliminar repetidos
inteirps = {1, 1, 2, 3, 5, 4, 6, 6, 7}
print(inteirps)

print('\n=======================\n')
carros = {'palio', 'gol', 'uno', 'uno'}
# dessa forma conseguimos colocar indices em sets
for indice, carros_lista in enumerate(carros):
    print(f'{indice}: {carros_lista}')

print('\n=======================\n')
print('\n=======================\n')
conjunto_a = {1, 3}
# união dos conjuntos
conjunto_b = {2, 4}
uniao = conjunto_a.union(conjunto_b)
print(uniao)

print('\n=======================\n')
# intersecção e conjuntos
conjunto_a = {1, 2, 3}

conjunto_b = {2, 4, 3}
uniao = conjunto_a.intersection(conjunto_b)
print(uniao)

print('\n=======================\n')
# diferença e conjuntos
conjunto_a = {1, 2, 3}

conjunto_b = {2, 4, 3}

diferenca = conjunto_a.difference(conjunto_b)
diferenca2 = conjunto_b.difference(conjunto_a)
print(diferenca)
print(diferenca2)

print('\n=======================\n')
# diferença simetrica e conjuntos
# pega itens que não se repetem ou fazem intersecção dos 2 conjuntos
conjunto_a = {1, 2, 3}

conjunto_b = {2, 4, 3}

diferenca = conjunto_a.symmetric_difference(conjunto_b)

print(diferenca)

print('\n=======================\n')
# subconjunto
# compara se um conjunto está dentro do outro
conjunto_a = {1, 2, 3}

conjunto_b = {2, 4, 3, 1}

subconjunto = conjunto_a.issubset(conjunto_b)
subconjunto2 = conjunto_b.issubset(conjunto_a)
print(subconjunto)
print(subconjunto2)

print('\n=======================\n')
# super cojunto
# compara se um conjunto está dentro do outro
conjunto_a = {1, 2, 3}

conjunto_b = {2, 4, 3, 1}

subconjunto = conjunto_a.issuperset(conjunto_b)
subconjunto2 = conjunto_b.issuperset(conjunto_a)
print(subconjunto)
print(subconjunto2)

print('\n=======================\n')
# disjunto quando não tem itens em comum
a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9}
c = {1, 0}
disjunto = a.isdisjoint(b)
print(disjunto)
disjunto2 = a.isdisjoint(c)
print(disjunto2)

print('\n=======================\n')
# adiciona item no conjunto
sorteio = {1, 23}
print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(74)
print(sorteio)
sorteio.add(1)
print(sorteio)
