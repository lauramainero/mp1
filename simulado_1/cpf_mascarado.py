cpf = input()

mascara = ''

for d in cpf:
    if int(d) % 2 == 0:
        mascara += '*'
    else:
        mascara += d
print(mascara)