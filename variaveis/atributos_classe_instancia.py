class Estudante:
    escola = "ETEC"  # Atributo de classe (ou atributo de classe)
    periodo = "noturno"  # Atributo de classe (ou atributo de classe)

    def __init__(self, nome, matricula):
        self.nome = nome  # Atributo de instância (ou atributo de objeto)
        self.matricula = matricula  # Atributo de instância (ou atributo de objeto)

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Escola: {self.escola}, Peíodo: {self.periodo}"  # Método especial para representar o objeto como string


# Criando uma instância da classe
Estudante1 = Estudante("João", "12345")
Estudante2 = Estudante("Maria", "67890")

print(Estudante1)  # Saída: Nome: João, Matrícula: 12345, Escola: ETEC
print(Estudante2)  # Saída: Nome: Maria, Matrícula: 67890, Escola: ETEC
Estudante.escola = "SENAI"  # Alterando o atributo de classe
Estudante.escola = "SENAI"  # Alterando o atributo de classe

print(Estudante1)  # Saída: Nome: João, Matrícula: 12345, Escola: SENAI
Estudante3 = Estudante("Carlos", "54321")
Estudante.periodo = "diurno"  # Alterando o atributo de classe
print(Estudante1)  # Saída: Nome: João, Matrícula: 12345, Escola: SENAI
print(Estudante3)  # Saída: Nome: João, Matrícula: 12345, Escola: SENAI
