class Sessao:
    def __init__(self, conta_ativa):
        self.conta_ativa = conta_ativa

    @property
    def conta(self):
        return self.conta_ativa
