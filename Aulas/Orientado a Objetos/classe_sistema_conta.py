class Conta:
    def __init__(self, saldo, nome):
        self.__saldo = saldo
        self.__nome = nome

    def mostrar(self):
        return f"Seu saldo: {self.__saldo}\nNome: {self.__nome}"

    def depositar(self, valor):
        self.__saldo += valor
        return f"Seu saldo: {self.__saldo}\nNome: {self.__nome}"

p1 = Conta(1000, "Nicolas")

print(p1.mostrar())