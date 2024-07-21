class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor_nova):
        self.__cor = cor_nova

    def mostrar_cor(self):
        return f"A cor da bola é {self.__cor}"

bola1 = Bola("Vermelho", "90cm", "borracha")
print(bola1.mostrar_cor())

bola1.troca_cor("Roxa")
print(bola1.mostrar_cor())