def mostrar(a, b, funcao):
    return print(f"Resultado = {funcao(a, b)}")

def soma(a, b):
    return a + b

mostrar(5, 5, soma)