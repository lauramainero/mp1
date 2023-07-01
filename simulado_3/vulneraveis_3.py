n_redes = int(input())

horas = []
minutos = []

for r in range(n_redes):
    h = int(input()) * 60
    m = int(input())

    horas.append(h)
    minutos.append(m)

total = sum(horas) + sum(minutos)
print(total)
