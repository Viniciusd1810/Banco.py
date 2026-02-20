from decimal import Decimal
from cliente import Cliente
from endereco import Endereco
from sessao import Sessao
from transacao import Deposito, Saque

clientes = {}
sessao = None


def menu_principal():
    print(
        """
    Banco
    [1] - Cadastrar Cliente
    [2] - Cadastrar Conta
    [3] - Logar na Conta
    [4] - Encerrar o Sistema
    """
    )


def menu_logado():
    print(
        """
    Banco
    [1] - Depositar
    [2] - Saque
    [3] - Transferência
    [4] - Extrato
    [5] - Deslogar
    """
    )


def cadastrar_cliente(clientes):
    cpf = input("Digite seu CPF:\n")
    if cpf in clientes:
        print("CPF já cadastrado")
        return None

    nome = input("Digite seu Primeiro Nome:\n")
    sobrenome = input("Digite seu sobrenome:\n")
    data_nascimento = input("Digite sua data de Nascimento\n")
    logradouro = input("Digite o logradouro de sua resideência:\n")
    numero = input("Digite o numero de sua residência:\n")
    bairro = input("Digite o bairro de sua residência:\n")
    cidade = input("Digite a Cidade de sua residência:\n")
    estado = input("Digite o a sigla do estado de sua residência:\n")

    endereco = Endereco(logradouro, numero, bairro, cidade, estado)
    cliente = Cliente(cpf, nome, sobrenome, data_nascimento, endereco)

    clientes[cpf] = cliente
    print("Cliente Cadastrado com Sucesso!")
    print(cliente)


def cadastrar_conta(clientes):
    cliente = input("Digite seu CPF:\n")
    if cliente not in clientes:
        print("Cliente não cadastrado")
        return None

    try:
        senha = int(input("Digite uma Senha númerica:\n"))
    except ValueError:
        print("Senha deve ser um valor numérico")
        return None

    clientes[cliente].criar_conta(senha)
    print("Conta cadastrada com Sucesso")


def logar(clientes):
    cliente = input("Digite seu CPF:")
    if cliente not in clientes:
        print("Cliente não cadastrado")
        return None
    clientes[cliente].listar_contas()

    try:
        conta_selecionada = int(input("Digite o numero da conta:\n"))
    except ValueError:
        print("Número de conta inválido")
        return None

    if conta_selecionada not in clientes[cliente].contas:
        print("Conta não existente")
        return None

    try:
        senha = int(input("Digite a senha da conta:"))
    except ValueError:
        print("Senha deve ser um valor numérico")
        return None

    conta_ativa = clientes[cliente].contas[conta_selecionada]
    senha_validada = conta_ativa.validar_senha(senha)

    if not senha_validada:
        print("Senha Inválida")
        return None
    sessao = Sessao(conta_ativa)
    print("Sessão Logada")
    return sessao


def depositar(sessao):
    try:
        valor_deposito = Decimal(input("Digite o valor que deseja Depositar\n"))
    except ValueError:
        print("Valor de Deposito deve ser um valor numerico")
        return None

    try:
        Deposito(valor_deposito).registrar(sessao.conta)
        print(f"Deposito Realizado com Sucesso\nSeu novo saldo é:{sessao.conta.saldo_formatado}")
    except ValueError as e:
        print(e)


def saque(sessao):
    try:
        valor_saque = Decimal(input("Digite o valor que deseja sacar\n"))
    except ValueError:
        print("Valor do Saque deve ser um valor numerico")
        return None

    try:
        Saque(valor_saque).registrar(sessao.conta)
        print(f"Saque Realizado com Sucesso\nSeu novo saldo é:{sessao.conta.saldo_formatado}")
    except ValueError as e:
        print(e)


def imprimir_extrato(sessao):
    for transacao in sessao.conta.historico.transacoes:
        print(transacao)
    print(f"Saldo Atual: {sessao.conta.saldo_formatado}")


system_on = True
while system_on is True:
    if sessao is None:
        menu_principal()
        operacao = input("Escolha uma operação:\n")
        match operacao:
            case "1":
                cadastrar_cliente(clientes)
            case "2":
                cadastrar_conta(clientes)
            case "3":
                sessao = logar(clientes)
            case "4":
                system_on = False
                print("Encerrando Sistema...")
            case _:
                print("Opção Inválida!")
    else:
        menu_logado()
        operacao = input("Escolha uma operação:\n")
        match operacao:
            case "1":
                depositar(sessao)
            case "2":
                saque(sessao)
            case "3":
                pass
            case "4":
                imprimir_extrato(sessao)
            case "5":
                sessao = None
                print("Sessão Deslogada...")
            case _:
                print("Opção Inválida!")
