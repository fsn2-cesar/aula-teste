arquivo = open("dados.txt", "r", encoding="utf-8")

for linha in arquivo:
    print(linha)

arquivo.close()
