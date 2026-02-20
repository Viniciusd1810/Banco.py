from datetime import date
from decimal import Decimal
from historico import Historico


class Conta:
    _contador_contas = 1

    def __init__(self, senha, agencia="0001"):
        self.agencia = agencia
        self.numero_conta = Conta._contador_contas
        Conta._contador_contas += 1
        self._senha = senha
        self._saldo = Decimal("0.00")
        self.limite_por_saque = Decimal("500.00")
        self.quantidade_saques_realizados = 0
        self.historico = Historico()
        self.data_ultimo_saque = None

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        return False

    @property
    def saldo(self):
        return self._saldo

    @property
    def saldo_formatado(self):
        return f"R$ {self._saldo:.2f}"

    def depositar(self, valor: Decimal):
        if valor <= Decimal("0.00"):
            raise ValueError("Valor do Deposito deve ser acima de R$ 0,00")
        self._saldo += valor

    def sacar(self, valor: Decimal):
        hoje = date.today()

        if valor <= Decimal("0.00"):
            raise ValueError("Valor do saque deve ser acima de R$ 0,00")

        if valor > self.saldo:
            raise ValueError("Saldo Insuficiente")

        if valor > self.limite_por_saque:
            raise ValueError("Valor de Saque excede o Valor permitido por Transação")

        if self.data_ultimo_saque != hoje:
            self.quantidade_saques_realizados = 0
            self.data_ultimo_saque = hoje

        if self.quantidade_saques_realizados >= 3:
            raise ValueError("Limite de Saque Diarios Permitido Alcançado")

        self._saldo -= valor
        self.quantidade_saques_realizados += 1

    def __str__(self):
        return f"Agência: {self.agencia} | Numero da Conta: {self.numero_conta} | Saldo: {self.saldo_formatado}"
