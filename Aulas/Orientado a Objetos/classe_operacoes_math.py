class Math():
    def __init__(self, valor, valor2):
        self.valor = valor
        self.valor2 = valor2

    def soma(self):
        return(self.valor + self.valor2)
    
    def sub(self):
        return(self.valor - self.valor2)

    def div(self):
        return(self.valor / self.valor2)

conta = Math(2, 3)
print(conta.soma())

conta = Math(10, 7)
print(conta.sub())

conta = Math(10, 2)
print(conta.div())