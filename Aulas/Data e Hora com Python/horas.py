from datetime import date, datetime

hora = date.today()
hora2 = datetime(2021, 12, 31, 10, 10, 10)
hora3 = datetime.now().strftime("%d/%m/%y %H:%M:%S")

print(hora)
print(hora2)
print(hora3)