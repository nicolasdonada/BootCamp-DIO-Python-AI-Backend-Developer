from pathlib import Path

ROOT_PATH = Path(__file__).parent
FILE_PATH = ROOT_PATH / 'texto.txt'

try:
    with open(FILE_PATH, 'w', encoding='utf-8') as arquivo:
        arquivo.write("BRASIL BRASIL BRASIL")

except IOError as exc:
    print(f"Não foi possivel abrir o arquivo {exc}")

except UnicodeDecodeError as exc:
    print(f"Caracteres inválidos {exc}")