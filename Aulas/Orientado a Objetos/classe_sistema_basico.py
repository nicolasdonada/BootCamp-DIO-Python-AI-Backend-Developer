class Banco():

    def __init__(self, conta):
        self.conta = conta

    def Func(self):
        print('BEM VINDO AO BANCO')
        while True:
            print('''
            1 - DEPOSITAR
            2 - SACAR
            3 - EXTRATO
            ''')

            op = int(input("Sua opção: "))

            if op == 1:
                valor_deposito = float(input("Valor: "))

                self.conta += valor_deposito
            
            if op == 2:
                valor_sacar = float(input("Valor: "))

                self.conta -= valor_sacar
            
            if op == 3:
                print(f'''
                EXTRATO DA CONTA
            
                SALDO: {self.conta}''')

conta_inicial = 0
banco_instance = Banco(conta_inicial)

banco_instance.Func()