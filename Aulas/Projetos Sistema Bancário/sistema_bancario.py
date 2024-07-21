saldo_bancario = 0
saque_diario = 0

while True:

    print(f" {' Opções ':=^20} ")
    print('''
    1 - Depositar
    2 - Sacar
    3 - Extrato
    ''')

    op_num = str(input("Digite sua opção: ")).strip()[0]
    while not op_num.isdecimal :
        op_num = str(input("Digite sua opção: ")).strip()[0]

    if op_num == "1":
        valor_deposito = float(input('Digite o valor desejado para depositar: R$'))
        
        saldo_bancario += valor_deposito

    if op_num == "2":
        if saque_diario >= 3:
            print("Limite de saque diário")

        else:
            valor_sacar = float(input('Digite o valor desejado para sacar: R$'))
            saque_diario += 1

            if valor_sacar > 500:
                print("Valor máximo de saque R$500")

            elif valor_sacar > saldo_bancario:
                print("O valor desejado para sacar é maior que seu saldo bancário.")

            else:
                saldo_bancario -= valor_sacar

    if op_num == "3":
        print(f"Seu saldo é: R${saldo_bancario:.2f}")
        
    