class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar(self, transacao):
        self._transacoes.append(transacao)

    @property
    def transacoes(self):
        return list(self._transacoes)
