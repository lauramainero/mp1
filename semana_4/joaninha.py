# so funciona com carga superior a 5%
# sensor 1: B para 'bateu' ou L para 'area livre'
# sensor 2: A para 'abismo' ou P para 'piso'
# comandos: 'virar' ou 'avançar'
# apos cada comando, avisar a porcentagem de bateria disponivel
# cada comando 'virar' consome 5% e cada comando 'avançar' consome 1% de bateria
# bateria indisponivel: 'recarregar'

# entrada: porcentagem de bateria disponivel para a joaninha
# loop: duas entradas para utilizar os pares de 'B ou L' e 'A ou P'
# saida: o comando e a porcentagem de bateria utilizada
    # 'virar: X%'

bateria = int(input())

while bateria > 5:
    s_1 = input() # B ou L
    s_2 = input() # A ou P

    if s_1 == 'B':
        bateria -= 5
        print('virar:', bateria)
    elif s_1 == 'L':
        if s_2 == 'A':
            bateria -= 5
            print('virar:', bateria)
        elif s_2 == 'P':
            bateria -= 1
            print('avançar:', bateria)
if bateria <= 5:
    print('recarregar:', bateria)