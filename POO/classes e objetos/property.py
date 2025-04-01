class Pessoa:
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self.ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        ano = 2025
        return ano - self.ano_nasc


pessoa = Pessoa("Lucas", 1990)
print(f"Meu nome é {pessoa.nome} e tenho {pessoa.idade} anos.")
print(pessoa.idade)
print(pessoa.nome)
