contatos = {
    'juniordefreitas1@gmail.com': {'nome': 'Junior', 'telefone': 1994552268},
    'michelledefreitas1@gmail.com': {'nome': 'Michelle', 'telefone': 1994552271},
}

# cria uma copia do dicionario mantendo o original intacto
copia_contatos = contatos.copy()

print(contatos)
print('\n')
print(' ♥ •'*12)
print('\n')


for quebra in contatos:
    print(quebra, end=('\n'))

print('\n')
print(' ♥ •'*12)
print('\n')

'''contatos.clear() #limpa o dicionario contatos
print(contatos)'''

print('\n')
print(' ♥ •'*12)
print('\n')

print(copia_contatos)
copia_contatos['juniordefreitas1@gmail.com'] = {
    'nome': 'José Quintino', 'telefone': 1994552268}
print(copia_contatos['juniordefreitas1@gmail.com'])

print('\n')
print(' ♥ •'*12)
print('\n')
# cria um dicionario passando a chave aí o valor vai ficar como none
teste_dic = dict.fromkeys(['nome', 'telefone'])
print(teste_dic)
# cria um dicionario passando a chave aí o valor vai ficar como 1981 para todos
teste_dic = dict.fromkeys(['nome', 'telefone'], 1981)
print(teste_dic)
print(teste_dic)
print(' ♥ •'*12)
ttr = copia_contatos.items()
print('TTR ', ttr)

kkeys = copia_contatos.keys()  # retorna só as chaves do dicionario
print(kkeys)

kkeys2 = copia_contatos.values()  # retorna só os valores do dicionario
print(kkeys2)
print(' ○ •'*12)
for auau in kkeys2:
    print(auau, end=('\n'))
print(' ○ •'*12)

print(' ♥ •'*12)
print(' ♥ •'*12)
copia_contatos.setdefault('idade', 570)
print(copia_contatos)

print(' ♥ •'*12)
print(' ♥ •'*12)
print(' ♥ •'*12)


verificado = 'telefone' in contatos['juniordefreitas1@gmail.com']
print(verificado)  # Saída esperada: True
