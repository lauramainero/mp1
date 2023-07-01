fila = []

while True:
    nome = input()

    if nome != '.':
        fila.append(nome)

    if nome == '.':
        break

print(fila)