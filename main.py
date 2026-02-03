quantidade_saque_diario = 0
numero_conta = 0
clientes = {}
sessao = None

def menu_principal():
    print("""
    Banco
    [1] - Cadastrar Cliente
    [2] - Cadastrar Conta
    [3] - Logar na Conta
    [4] - Encerrar o Sistema
    """)
    
def menu_logado():
    print("""
    Banco
    [1] - Depositar
    [2] - Saque
    [3] - Extrato
    [4] - Deslogar
    """)
    
def cadastrar_cliente(clientes):
    cpf = input("Digite seu CPF:\n")
    if cpf not in clientes:
        nome = input("Digite seu Primeiro Nome:\n")
        sobrenome = input("Digite seu sobrenome:\n")
        data_nascimento = input("Digite sua data de Nascimento\n")
        enderoco_logradouro = input("Digite o logradouro de sua resideência:\n")
        endereco_numero = input("Digite o numero de sua residência:\n")
        endereco_bairro = input("Digite o bairro de sua residência:\n")
        endereco_cidade = input("Digite a Cidade de sua residência:\n")
        endereco_estado = input("Digite o a sigla do estado de sua residência:\n")
        
        clientes[cpf] = {
            "nome_completo":{
                "nome": nome,
                "sobrenome": sobrenome
            },
            "data_de_nascimento": data_nascimento,
            "endereco":{
                "logradouro": enderoco_logradouro,
                "numero": endereco_numero,
                "bairro": endereco_bairro,
                "cidade": endereco_cidade,
                "estado": endereco_estado
            }
        }
        print("Cliente Cadastrado com Sucesso!")
    else:
        print("CPF já cadastrado")

def cadastrar_conta(clientes, numero_conta):
    cliente = input("Digite seu CPF:\n")
    if cliente in clientes:
        senha = int(input("Digite uma Senha númerica:\n"))
        numero_conta += 1
        if "contas" not in clientes[cliente]:
            clientes[cliente]["contas"] = {}
            clientes[cliente]["contas"][numero_conta] = {
                "agencia": "01",
                "senha": senha,
                "saldo": 0,
                "extrato": ""
            }
        else:
            clientes[cliente]["contas"][numero_conta] = {
                "agencia": "01",
                "senha": senha,
                "saldo": 0,
                "extrato": ""
            }
    else:
        print("Cliente não cadastrado")
    return numero_conta

def logar(clientes, sessao):
    cliente = input("Digite seu CPF:")
    if cliente in clientes and "contas" in clientes[cliente]:
        print(clientes[cliente]["contas"])
        escolha_conta = int(input("Digite o numero da conta:\n"))
        if escolha_conta in clientes[cliente]["contas"]:
            senha = int(input("Digite a senha da conta:"))
            if senha == clientes[cliente]["contas"][escolha_conta]["senha"]:
                sessao = {
                    "cliente_ativo": cliente,
                    "conta_ativa": escolha_conta
                }
                print("Sessão Logada")
            else:
                print("Senha Inválida")
        else:
            print("Conta não existente")
    else:
        print("Cliente não cadastrado")
    return sessao


def depositar(clientes, sessao):
    valor_deposito = float(input("Digite o valor que deseja Depositar\n"))
    if(valor_deposito >= 0):
        conta = clientes[sessao["cliente_ativo"]]["contas"][sessao["conta_ativa"]]
        conta["saldo"] += valor_deposito
        conta["extrato"] += (f"+ R$ {valor_deposito:.2f}\n")
        print(f"Deposito Realizado com Sucesso\nSeu novo saldo é:{conta["saldo"]:.2f}")
    else:
        print("Valor do Deposito deve ser acima de R$ 0,00")

def saque(clientes, sessao, quantidade_saque_diario):
    LIMITE_MAXIMO_POR_SAQUE = 500
    valor_saque = float(input("Digite o valor que deseja sacar\n"))
    conta = clientes[sessao["cliente_ativo"]]["contas"][sessao["conta_ativa"]]
    
    if(valor_saque <= 0):
        print("Valor do saque deve ser acima de R$ 0,00")
        return
    if(valor_saque > conta["saldo"]):
        print("Saldo Insuficiente")
        return
    
    if(valor_saque > LIMITE_MAXIMO_POR_SAQUE):
        print("Valor de Saque excede o Valor permitido por Transação")
        return
    
    if(quantidade_saque_diario==3):
        print("Limite de Saque Diarios Permitido Alcançado")
        return
    
    conta["saldo"] -= valor_saque
    quantidade_saque_diario += 1
    conta["extrato"] += (f"- R$ {valor_saque:.2f}\n")
    print(f"Saque Realizado com Sucesso\nSeu novo saldo é:{conta["saldo"]:.2f}")
    
    return quantidade_saque_diario

def imprimir_extrato(clientes, sessao):
    conta = clientes[sessao["cliente_ativo"]]["contas"][sessao["conta_ativa"]]
    print(conta["extrato"])
    print(f"Saldo Atual: {conta["saldo"]:.2f}")
    
system_on = True
while(system_on == True):
    if sessao == None:
        menu_principal()
        operacao = input("Escolha uma operação:\n")
        match operacao:
            case "1":
                cadastrar_cliente(clientes)
            case "2":
                numero_conta = cadastrar_conta(clientes, numero_conta)
            case "3":
                sessao = logar(clientes, sessao)
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
                depositar(clientes, sessao)
            case "2":
                quantidade_saque_diario = saque(clientes, sessao, quantidade_saque_diario)
            case "3":
                imprimir_extrato(clientes, sessao)
            case "4":
                sessao = None
                print("Sessão Deslogada...")
            case _:
                print("Opção Inválida!")
