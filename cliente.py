from conta import Conta


class Cliente:
    def __init__(self, cpf, nome, sobrenome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = {}

    def criar_conta(self, senha):
        conta = Conta(senha)
        self.contas[conta.numero_conta] = conta
        return conta

    def listar_contas(self):
        for conta in self.contas.values():
            print(conta)

    def realizar_transacao(self, conta, transacao):
        pass

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def __str__(self):
        return f"""
    Nome:{self.nome_completo}[{self.cpf}]
    Data Nascimento:{self.data_nascimento}
    Endereço:{self.endereco}
    """
