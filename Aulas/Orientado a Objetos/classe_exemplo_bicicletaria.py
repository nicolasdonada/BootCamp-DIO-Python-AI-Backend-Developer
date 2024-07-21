class Bicicletaria:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor
    
    def buzinar(self):
        print("Buzinando...")

    def parar(self):
        print("Parando...")

    def correr(self):
        print("Correndo...")

joao = Bicicletaria("Laranja", "Monark", 1990, 2000)

joao.buzinar()