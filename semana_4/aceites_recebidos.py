aceites = 0

while True:
    resultado = input()

    if resultado == 'accepted':
        aceites += 1

    if resultado == 'timeout':
        break
print(aceites)