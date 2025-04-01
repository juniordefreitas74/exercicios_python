class Bicicleta:  # classe Bicicleta
    def __init__(self, cor, modelo, ano, valor, aro=18):  # método construtor
        self.cor = cor  # atributo cor
        self.modelo = modelo  # atributo modelo
        self.ano = ano  # atributo ano
        self.valor = valor  # atributo valor
        self.aro = aro  # atributo aro

    def buzinar(self):  # método(ou função) buzinar
        print("BIBI")  # ação

    def parar(self):  # método(ou função) parar
        print("A bicicleta parou")  # ação

    def correr(self):  # método(ou função) correr
        print("A bicicleta está correndo")  # ação

    # def __str__(self):
    #   return f"Cor: {self.cor}\nModelo: {self.modelo}\nAno: {self.ano}\nValor: {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta(
    "vermelha", "Caloi", 2020, 500
)  # criando um objeto b1 da classe Bicicleta
b1.correr()  # chamando o método correr
b1.buzinar()  # chamando o método buzinar
b1.parar()  # chamando o método parar
print("\nCor:", b1.cor, "\nModelo:", b1.modelo, "\nAno:", b1.ano, "\nValor:", b1.valor)
print("*" * 50)
b2 = Bicicleta("verde", "monark", 2000, 189)  # criando um objeto b2 da classe Bicicleta
b2.correr()  # chamando o método correr
b2.buzinar()  # chamando o método buzinar
b2.parar()  # chamando o método parar
print("*" * 50)
print(b2)  # chamando o método __str__
print("*" * 50)
print(b1)  # chamando o método __str__
