'''from random import randint

valor_misterioso = randint(1, 10)

print("Valor misterioso gerado!")


while True:
  tentativa = int(input('Tente adivinhar: '))
  
  if tentativa > valor_misterioso:
    print('valor misterioso menor!')

  if tentativa < valor_misterioso:
    print('Valor misterioso maior!')

  if tentativa == valor_misterioso:
    print('Parabéns você acertou!!')
    break'''

'''velocidade_condutor = float(input('Digite sua velocidade: '))

if velocidade_condutor < 80:
  print('não houve multa')

if velocidade_condutor >= 80 and velocidade_condutor <= 90:
  print('levou multa leve')

if velocidade_condutor >= 91 and velocidade_condutor <= 100:
  print('levou multa grave')

if velocidade_condutor > 100:
  print('Levou multa gravissima')'''

'''nu = 1
fac = 5

for n in range(fac, 0, -1):
  nu *= n
  print(n, end=" x ")

print(f"= {nu}")'''

'''v1 = 3
v2 = 7
v3 = 1

print(max(v1, v2, v3))
print(min(v1, v2, v3))'''

lista1 = []

for n in range (1, 4):
  n1 = int(input('Digite valores:'))
  lista1.append(n1)

menor_valor = lista1[0]
maior_valor = lista1[0]

for v in lista1:
  if v < menor_valor:
    menor_valor = v
  if v > maior_valor:
    maior_valor = v

print(maior_valor)
print(menor_valor)

