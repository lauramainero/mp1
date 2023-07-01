n_alunas = int(input())

aprovadas = []
reprovadas = []

for a in range(n_alunas):
    n_exercicios = int(input())

    if n_exercicios >= 3:
        aprovadas.append(a)
    else:
        reprovadas.append(a)

print('Aprovadas:', len(aprovadas))
print('Recuperação:', len(reprovadas))