# entrada: entre 1 e 6 linhas
    # a ultima contem o valor 0
    # as demais contem o valor de uma nota
# saida: valor total das notas

total_notas = []

while len(total_notas) <= 6:
    nota = int(input())

    if nota == 0:
        break

    total_notas.append(nota)
print(sum(total_notas))