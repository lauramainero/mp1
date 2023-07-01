total_resultados = ['No', 'No', 'No', 'No']

while True:
    resultado = input()

    if resultado.startswith('accepted'):
        if resultado.endswith('1'):
            total_resultados[0] = 'Yes'
        elif resultado.endswith('2'):
            total_resultados[1] = 'Yes'
        elif resultado.endswith('3'):
            total_resultados[2] = 'Yes'
        elif resultado.endswith('4'):
            total_resultados[3] = 'Yes'
    elif resultado == 'timeout':
        break

print(*total_resultados, sep=' ')

