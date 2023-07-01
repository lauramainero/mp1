# leitura sempre começa com o sensor no estado 'parado'
# o programa termina quando é lido o valor 'f'
# o valor 'p' indica que o sensor informa que o dispositivo está parado
# o valor 'm' indica que o sensor informa que o dispositivo está em movimento

# o usuário está ativo quando o número de leituras que indicam movimento é maior que o de leituras que indicam parado
# note que o dispositivo já começa parado

# entrada:
    # um número interminado de linhas com os valores 'm' e 'p'
    # a última linha tem o valor 'f'

situacao = input()

parado = 1
movimento = 0

while situacao != 'f':
    if situacao == 'p':
        parado += 1
    elif situacao == 'm':
        movimento += 1
    situacao = input()

    if situacao == 'f':
        break

if parado >= movimento:
    print('sedentário')
elif movimento > parado:
    print('ativo')