alunas = []

while True:
    nome = input()

    if nome == '.':
        break
    alunas.append(nome)

meio = len(alunas) // 2

alunas.sort()

if len(alunas) % 2 == 0:
    nome_meio1 = alunas[meio - 1]
    nome_meio2 = alunas[meio]
    print(nome_meio1)
    print(nome_meio2)
elif len(alunas) % 2 != 0:
    nome_meio = alunas[meio]
    print(nome_meio)


