n_linha = 0

while True:
    linha = input()
    if linha == "CDA 1942":
        break
    elif linha.strip():
        n_linha += 1

print(n_linha)