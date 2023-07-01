alunas = []

while True:
    nome = input()

    if nome == '.':
        break

    alunas.append(nome)
alunas.sort()

print(alunas[0])
print(alunas[-1])