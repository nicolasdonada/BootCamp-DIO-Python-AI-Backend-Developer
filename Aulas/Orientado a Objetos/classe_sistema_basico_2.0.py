class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo


    @property
    def mostrar_saldo(self):
        return self.__saldo

    @mostrar_saldo.setter
    def depositar_saldo(self, saldo):
        if not isinstance(saldo, (int, float)):
            raise ValueError('Valor precisa ser númerico')  
        else:
            self.__saldo += saldo
    
    @mostrar_saldo.setter
    def sacar_saldo(self, saldo):
        if not isinstance(saldo, (int, float)):
            raise ValueError('Valor precisa ser numerico')
        else:
            self.__saldo -= saldo

Minha_conta = Conta(0)

while True:
    print('1 - Mostrar saldo\n2 - Depositar saldo\n3 - Sacar saldo\n4 - Sair')

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        print(f'Seu saldo é: R${Minha_conta.mostrar_saldo}')

    elif opcao == 2:
        valor = int(input(f'Digite o valor para depositar: R$'))
        Minha_conta.depositar_saldo = valor

    elif opcao == 3:
        valor = int(input(f'Digite o valor para sacar: R$'))
        Minha_conta.sacar_saldo = valor
    
    elif opcao == 4:
        break