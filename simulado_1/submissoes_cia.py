n_problemas = int(input())

submissoes = 0
aceitos = 0

while aceitos < n_problemas:
    resultado = input()

    if resultado == 'accepted':
        submissoes += 1
        aceitos += 1
    elif resultado == 'error':
        submissoes += 1

    if resultado == 'timeout':
        break
print('submissoes:', submissoes)
print('aceitos:', aceitos)