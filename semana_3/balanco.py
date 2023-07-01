n_mov = int(input())

mov = [ ]

for _ in range(n_mov):
    saldo = float(input())
    mov.append(saldo)

balanco = sum(mov)

print('%.2f' % balanco)
