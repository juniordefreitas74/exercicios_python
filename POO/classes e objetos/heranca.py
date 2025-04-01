class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Motor ligado")

    def __str__(self):
        return f" {self.__class__.__name__} cor= {self.cor}, placa= {self.placa}, numero_rodas= {self.numero_rodas}"

    # retorna uma string com os atributos da classe


class Motocicleta(Veiculo):
    def empinar(self):
        print("A motocicleta está empinando.")


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def estar_carregado(self):
        print("O caminhão está carregado.")


moto = Motocicleta("preto", "ABC-1234", 2)

carro = Carro("branco", "DEF-1645", 4)

caminhao = Caminhao("azul", "GHI-7890", 6)

print(moto)
print(caminhao)
print(carro)
