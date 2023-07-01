alunas = int(input())

notas = []

for _ in range(alunas):
    n = float(input())

    notas.append(n)

notas.sort(reverse=True)
print(notas)

