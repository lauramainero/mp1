n_alunas = int(input())

alunas = []

for _ in range(n_alunas):
    nome = input()

    alunas.append(nome)

alunas.sort()
print(alunas)