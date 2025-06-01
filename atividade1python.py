menu = """

    Digite um Valor:

    [1] Depósito
    [2] Saco
    [3] Extrato
    [4] Sair

    -> """

saldo = 0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito():
    valor = float(input("Digite o valor a ser depositado: "))
    if valor > 0:
        return valor
    else:
        print("Valor inválido.")
        return 0

def extrato(saldo):
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def sacar(saldo, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
        return saldo, numero_saques

    valor = float(input("Digite o valor para saque: "))

    if valor > limite:
        print("Erro: valor do saque excede o limite permitido de R$ 500")
    elif valor > saldo:
        print("Erro: saldo insuficiente.")
    elif valor <= 0:
        print("Erro: valor inválido para saque.")
    else:
        saldo -= valor
        numero_saques += 1
        print("Saque realizado com sucesso!")

    return saldo, numero_saques

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = deposito()
        if valor > 0:
            saldo += valor
            print("Depositado com sucesso!")

    elif opcao == 2:
        saldo, numero_saques = sacar(saldo, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == 3:
        extrato(saldo)

    elif opcao == 4:
        print("Sistema Offline!")
        break

    else:
        print("Opção Inválida, escolha novamente")
