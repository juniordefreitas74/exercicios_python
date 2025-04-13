class Passaro:
    def voar(self):
        print("está voando.")


class Pardal(Passaro):
    def voar(self):
        return Passaro().voar()  # ou super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("não voa.")
        # super().voar()# super() chama o método da classe pai


def plano_voo(qualquer_coisa):
    qualquer_coisa.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
