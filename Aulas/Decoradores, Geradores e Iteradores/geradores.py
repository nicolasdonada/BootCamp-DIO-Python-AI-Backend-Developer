conta = [{"conta": "Nick", "historico": ["Déposito R$100", "Saque R$200"]}]

for c in conta:
    for cada in c["historico"]:
        if "Saque" in cada:
            print(cada)
        