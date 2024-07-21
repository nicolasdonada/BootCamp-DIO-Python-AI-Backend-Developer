from datetime import datetime


def meudecorador(func):
    def logs(*args, **kwargs):
        func(*args, **kwargs)
        if "deposito" in func:
            print("Tipo de transação: Depósito")

        print(f'Data da transação: {datetime.now().strftime("%d/%m/%y %H:%M:%S")}')

    return logs

@meudecorador
def sacar(valor):
    print(f"Valor sacado {valor}")
    print("Tipo de transação: Saque")
    

@meudecorador
def deposito(valor):
    print(f"Valor depositado {valor}")
    

@meudecorador
def criar_conta():
    print("Tipo de transação: Conta criada")

deposito(10)
