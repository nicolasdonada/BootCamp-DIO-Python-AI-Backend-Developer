def menu():
    print('''
    ====== Menu ======
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Criar cliente
    5 - Criar conta corrente
    6 - Listar contas
    7 - Sair
    ''')

    op = str(input("Digite sua opção: "))
    if not op.isdecimal():
        op = str(input("Digite sua opção: "))
    
    return op

def sacar(saldo, valor, extrato, limite, saque_quant, limite_saque):
    if saque_quant == limite_saque:
        print("\n--- Operação falhou! Limite de saque atingido. ---")
    
    elif valor > limite:
        print("\n--- Operação falhou! Limite de valor de saque atingido. ---")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")
    
    return saldo, extrato




def depositar(saldo, valor_deposito, extrato):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\tR${valor_deposito:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n--- Operação falhou! O valor informado é inválido. ---")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("======== EXTRATO ========")
    print("Não há movimentações aqui." if not extrato else extrato)
    print("=========================")
    print(f"Saldo na conta: R${saldo:.2f}")
    print("=========================")

def criar_cliente(clientes):
    cpf = input(("Digite seu CPF: "))

    cliente = filtrar_cliente(clientes, cpf)

    if cliente:
        print("\n===== CPF já cadastrado =====")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({'nome': nome, 'data_nascimento': data_nascimento, "endereco": endereco, "cpf": cpf})

    print("===== Cliente cadastrado com sucesso! =====")

def filtrar_cliente(clientes, cpf):
    filtros = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    
    return filtros[0] if filtros else None
        

def criar_conta(agencia, num_conta, clientes):
    cpf = input(("Informe seu cpf: "))
    cliente = filtrar_cliente(clientes, cpf)

    if cliente:
        print("===== Conta cadastrada com sucesso! =====")
        return {"agencia": agencia, "conta": num_conta, "cliente": cliente}
        
    
    print("\n===== Usuário não encontrado, fluxo de criação de conta encerrado! =====")

def listar_contas(contas):
    for c in contas:
        print(f'''
            \n===== Lista de Contas =====
            \nConta: {c['conta']}
Agência: {c['agencia']}
Nome: {c['cliente']['nome']}
            ''')

def main():
    saldo_bancario = 0
    extrato = ""
    saques = 0
    saque_diario = 3
    limite = 500
    clientes = []
    contas = []
    agencia = "0001"

    while True:

        opcao = menu()

        if opcao == "1":
            valor_depositar = float(input('Digite o valor para depositar: R$'))
            
            saldo_bancario, extrato = depositar(saldo_bancario, valor_depositar, extrato)
            print(saldo_bancario)

        if opcao == "2":
            valor_sacar = float(input('Digite o valor para sacar: R$'))

            saldo_bancario, extrato = sacar(saldo_bancario, valor_sacar, extrato, limite, saques, saque_diario)
            saques += 1
        
        if opcao == "3":
            exibir_extrato(saldo_bancario, extrato)
        
        if opcao == "4":
            criar_cliente(clientes)

        if opcao == "5":
            num_conta = len(contas) + 1

            conta = criar_conta(agencia, num_conta, clientes)

            if conta:
                contas.append(conta)

        if opcao == "6":
            listar_contas(contas)

        if opcao == "7":
            print("===== Saindo.... ======")
            break

main()