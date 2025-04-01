class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostra_saldo(self):
        return self._saldo


conta = Conta(100)
conta.depositar(50)
conta.nro_agencia = 1000  # Atributo público, pode ser acessado diretamente
print(conta.mostra_saldo())
print(f"Agência número: {conta.nro_agencia}")  # Acesso direto ao atributo público
conta.sacar(30)
print(conta.mostra_saldo())
