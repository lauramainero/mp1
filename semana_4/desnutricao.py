peso_n = 0
peso_ab = 0
peso_ac = 0

while True:
    peso = input()

    if peso == 'X':
        peso_ab += 1
    elif peso == 'M':
        peso_ac += 1
    elif peso == 'N':
        peso_n += 1
    
    if peso == '.':
        break
    total = peso_ab + peso_ac + peso_n

print('Abaixo do peso:', peso_ab)
print('Peso normal:', peso_n)
print('Acima do peso:', peso_ac)
print('Total de crianças:', total)
