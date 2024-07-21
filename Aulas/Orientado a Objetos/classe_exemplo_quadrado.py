class Quadrado:
    def __init__(self, tamanho_lados):
        self.tamanho_lados = tamanho_lados

    def mudar_lado(self, novo_lado):
        self.tamanho_lados = novo_lado

    def mostrar_lado(self):
        return f"O tamanho do lado é {self.tamanho_lados}"

    def calcular_area(self):
        area_quadrado = self.tamanho_lados ** 2

        return f"A área do quadrado é: {area_quadrado}"

qua = Quadrado(10)

print(qua.mostrar_lado())
print(qua.calcular_area())

qua.mudar_lado(20)

print(qua.mostrar_lado())
print(qua.calcular_area())