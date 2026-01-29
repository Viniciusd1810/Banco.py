saldo = 0
extrato = ""
quantidade_saque_diario = 0

def menu():
    print("""
    Banco
    [1] - Depositar
    [2] - Saque
    [3] - Extrato
    [4] - Cadastrar Cliente
    [5] - Cadastrar Conta
    [6] - Encerrar o Sistema
    """)

def depositar(saldo, extrato):
    valor_deposito = float(input("Digite o valor que deseja Depositar\n"))
    if(valor_deposito > 0):
        saldo += valor_deposito
        print(f"Deposito Realizado com Sucesso\nSeu novo saldo é:{saldo:.2f}")
    else:
        print("Valor do Deposito deve ser acima de R$ 0,00")
    return saldo, extrato

def saque(saldo, extrato, quantidade_saque_diario):
    LIMITE_MAXIMO_POR_SAQUE = 500

    valor_saque = float(input("Digite o valor que deseja sacar\n"))
    if(valor_saque < saldo and valor_saque <= LIMITE_MAXIMO_POR_SAQUE and quantidade_saque_diario<3):
        saldo -= valor_saque
        print(f"Saque Realizado com Sucesso\nSeu novo saldo é:{saldo:.2f}")
        quantidade_saque_diario += 1
    elif(valor_saque > saldo):
        print("Saldo Insuficiente")
    elif(valor_saque > LIMITE_MAXIMO_POR_SAQUE):
        print("Valor de Saque excede o Valor permitido por Transação")
    elif(quantidade_saque_diario==3):
        print("Limite de Saque Diarios Permitido Alcançado")
    return saldo, extrato, quantidade_saque_diario

def extrato():
    print(f"Saldo Atual: {saldo}")
    
#def cadastrar_cliente():

#def cadastrar_conta():

system_on = True
while(system_on == True):
    menu()
    operação = int(input("Escolha uma operação:\n"))
    
    match operação:
        case 1:
            saldo, extrato = depositar(saldo, extrato)
        case 2:
            saldo, extrato, quantidade_saque_diario = saque(saldo, extrato, quantidade_saque_diario)
        case 3:
            extrato()
        case 4:
            cadastrar_cliente()
        case 5:
            cadastrar_conta()
        case 6:
            system_on = False
            print("Encerrando Sistema...")
        case _:
            print("Opção Inválida!")
