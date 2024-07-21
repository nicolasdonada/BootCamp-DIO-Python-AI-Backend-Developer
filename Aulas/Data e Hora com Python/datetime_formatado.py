'''
pessoa = {
    'nome' : 'Nicolas',
    'idade' : 18,
    'apelido' : 'Nick'
}

s = ('Meu nome é {nome}, tenho {idade} anos de idade, e meu apelido é {apelido}')

print(s.format(**pessoa))

print(f'Meu nome é {pessoa["nome"]}, tenho {pessoa["idade"]} anos de idade, e meu apelido é {pessoa["apelido"]}')

print('{!r}'.format('Ração'))

nome = 'ração'

print(f'{nome.upper()=}')
print(f'{nome=!a}')
print(f'{nome=!r}')

nome = ['Pedro', 'Marcelo', 'Luiz']
idade = [14, 17, 20]

for nome, idade in zip(nome, idade):
    print(f'{nome:-^10} {idade:4}')

string = str(input('Seu nome: '))

print(f'{string.upper()=!r:*^15}')

print(f"{15:-^20b}")

from math import pi

print(f" {pi:-^20.10f} ")
'''

from datetime import datetime

agora = datetime.now()
print(f'{agora: %d/%m/%Y %H:%M:%S}')
print(f'{agora: %H:%M:%S}')
print(f'{agora: %c}')