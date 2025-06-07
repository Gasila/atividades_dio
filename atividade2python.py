import datetime

usuarios = []
contas = []

LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0

def criar_usuario():
    cpf = input("CPF (somente números): ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        print("Usuário já existe.")
        return

    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    print("✅ Usuário criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": "0001",
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0.0,
        "saques": 0,
        "historico": []
    })
    print(f"✅ Conta {numero_conta} criada com sucesso!")

def deposito(conta):
    valor = float(input("Valor para depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conta["historico"].append(f"{agora}: Depósito de R$ {valor:.2f}")

        print("💰 Depositado com sucesso!")
    else:
        print("Valor inválido.")

def sacar(conta):
    if conta["saques"] >= LIMITE_SAQUES:
        print("❌ Limite diário de saques atingido.")
        return

    valor = float(input("Valor para saque: "))

    if valor > conta["saldo"]:
        print("❌ Saldo insuficiente.")
    elif valor > LIMITE_VALOR_SAQUE:
        print("❌ Limite por saque é R$ 500.00.")
    elif valor <= 0:
        print("❌ Valor inválido.")
    else:
        conta["saldo"] -= valor
        conta["saques"] += 1
        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conta["historico"].append(f"{agora}: Saque de R$ {valor:.2f}")

        print("💸 Saque realizado com sucesso!")

def visualizar_extrato(conta):
    print("\n📄 Histórico de transações:")
    for evento in conta["historico"]:
        print(" -", evento)
    print(f"\n💰 Saldo atual: R$ {conta['saldo']:.2f}")

def selecionar_conta():
    if not contas:
        print("⚠️ Nenhuma conta criada ainda.")
        return None

    for c in contas:
        print(f"{c['numero']}: {c['usuario']['nome']} (CPF: {c['usuario']['cpf']})")

    numero = int(input("Digite o número da conta: "))
    conta = next((c for c in contas if c["numero"] == numero), None)

    if not conta:
        print("❌ Conta não encontrada.")
    return conta

# Menu principal
while True:
    opcao = input("""
    ======================
        MENU BANCÁRIO
    ======================
    [1] Criar Usuário
    [2] Criar Conta
    [3] Acessar Conta
    [4] Sair
    => """)

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        criar_conta()

    elif opcao == "3":
        conta = selecionar_conta()
        if conta:
            while True:
                acao = input("""
    [1] Depositar
    [2] Sacar
    [3] Ver Extrato
    [4] Voltar
    => """)
                if acao == "1":
                    deposito(conta)
                elif acao == "2":
                    sacar(conta)
                elif acao == "3":
                    visualizar_extrato(conta)
                elif acao == "4":
                    break
                else:
                    print("Opção inválida.")

    elif opcao == "4":
        print("Sistema finalizado.")
        break
    else:
        print("Opção inválida.")
