# dicionário sempre tem que ter chae e valor
pessoa = {'nome': 'Junior', 'idade': 50}
print(pessoa)

print('\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')

pessoa = dict(nome='Michelle', idade=43)
print(pessoa)

print('\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')
# adiciona iten no dicionário
pessoa['telefone'] = '99455-2271'

print(pessoa)

print('\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

print('\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')
print('\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')

contatos = {
    'juniordefreitas1@gmail.com': {'nome': 'Junior', 'telefone': 1994552268, },
    'michelledefreitas1@gmail.com': {'nome': 'Michelle', 'telefone': 1994552271, },
}

print(contatos['juniordefreitas1@gmail.com']['telefone'])

print('\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')

for teste in contatos:
    print(teste)


print('\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n')

for teste in contatos:
    print(teste, contatos[teste])

print(' * *' * 20)


for nome, itens in contatos.items():
    print(nome, itens)


print(' • ○ ♥'*12)
print(' • ○ ♥'*12)


