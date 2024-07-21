from datetime import datetime

lista = []

for a in range (0,6):
    lista.append(datetime.now().strftime("%d/%m/%y"))

for c in lista:
    if c == datetime.now().strftime("%d/%m/%y"):
        print(c)