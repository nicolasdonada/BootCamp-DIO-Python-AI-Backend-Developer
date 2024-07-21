def escreva(func):
    def escreva_bonito(*args, **kwargs):
        print("Iniciado")
        func(*args, **kwargs)
        print("Finalizado")

    return escreva_bonito

@escreva
def f1(x):
    print(f"O x é {x}")

@escreva
def f2():
    print(f"O x é 0")


print()
f1(10)
print()
f2()
print()
