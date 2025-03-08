#While expressão booleana:
# siginifica:
# Execute este código até que a expressão booleana seja falsa 

'''a = 0
while a < 10: # repita 'a' enquanto for menor que 10 
    print('Valor de a: ' + str(a)) #dessa forma tem que converter o a (numero int) para string pois não concatena (+) str e int
    a += 1 #acrescenta 1 em a'''
    
'''while a < 10:
    print(f'Valor de a: {a}') # dessa forma usando fstring não precisa converter para str o int a
    a +=1'''
    
print('====================================================')
    
vogais = ['a','e','i','o','u']
familia = ['Michelle', "Junior", 'Lara']
    
print (vogais[:])

print('===================FOR==========================')
for letras in vogais: #coloque em letras cada item da lista vogais
    print(letras)
    
    
print('====================FOR=============================')
for indice, item in enumerate (vogais): #coloque em indice  cada item da lista vogais e mostre a posição
    print(indice,item)

print('====================FOR===========================')
vogais = ['a','e','i','o','u','w']
for letras in range(5): # coloque em letras os elementos da posição 0 ate a 4 de vogais
    print(vogais[letras])

print('====================WHILE===========================')
i=0
while i <5: #enquanto i for menor que 5
    print(i,vogais[i])# imprime a posição de i 
    # depois ele imprime o item da lista vogais referente a posição i
    # quando acrescenta 1 ele incrementa e faz a mesma coisa o numero de vezes colocado no while
    i +=1

print('====================WHILE===========================')
idade = 0
while idade < 60:
    print(idade, end=(''))
    idade +=1
else:
    print('\nVOCÊ É UMA PESSOA IDOSA')
print('====================for===========================')
print('====================for===========================')

for Freitas in familia:
    print(Freitas ,end=(' - \n'))
    
    
print('====================for===========================')
print('====================for===========================')

minha_lista = ['a', 'b', 'c']
for indice, valor in enumerate(minha_lista): #coloque em indice  cada item da lista vogais e mostre a posição
    print(f"O elemento no índice {indice} é {valor}")