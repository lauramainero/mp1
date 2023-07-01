total_pontos = 0

while True:
    pontos = int(input())

    if pontos == 0:
        print('>8)')
        break
    elif pontos < 0:
        total_pontos += pontos
        
        if total_pontos < 0:
            print('>8(')
            break
    else:
        total_pontos += pontos