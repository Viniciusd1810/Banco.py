from datetime import datetime
from decimal import Decimal
from abc import ABC, abstractmethod


class Transacao(ABC):
    def __init__(self, valor: Decimal):
        self.valor = valor
        self.data_hora = datetime.now()

    def registrar(self, conta):
        self.aplicar(conta)
        conta.historico.adicionar(self)

    @abstractmethod
    def aplicar(self, conta):
        pass

    def __str__(self):
        data_formatada = self.data_hora.strftime("%d/%m/%Y %H:%M")
        valor_formatado = f"R$ {self.valor:.2f}"

        return f"{data_formatada} | {self.tipo} | {valor_formatado}"


class Deposito(Transacao):
    tipo = "DEPOSITO"

    def aplicar(self, conta):
        conta.depositar(self.valor)


class Saque(Transacao):
    tipo = "SAQUE"

    def aplicar(self, conta):
        conta.sacar(self.valor)
