def calculadora():
    entrada1 = int(input('Digite um número: '))
    operacao = (input('Escolha uma operação (+ - * /): '))
    entrada2 = int(input('Digite um número: '))
    if operacao == '-':
        resultado = entrada1 - entrada2
    elif operacao == '+':
        resultado = entrada1 + entrada2
    elif operacao == '*':
        resultado = entrada1 * entrada2
    elif operacao == '/':
        if entrada2 == 0:
            return ('Erro: divisão por zero!')
        else:
            resultado = entrada1 / entrada2
    else:
        return ('Operação inválida')

    return f'O resultado é: {resultado}'


print(calculadora())
