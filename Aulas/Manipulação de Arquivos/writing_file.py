from pathlib import Path
import os

ROOT_PATH = Path(__file__).parent
FILE_PATH = ROOT_PATH / 'texto2.txt'



if os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'a', encoding='utf-8') as arquivo:
        arquivo.write('HELLO MY FRIENDS, MY NAME IS HARRY POTTER.\n')

    with open(FILE_PATH, 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

else:
    print('Arquivo não encontrado!')