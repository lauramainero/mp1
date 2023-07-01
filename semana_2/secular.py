ano = int(input())
if (ano % 10) == 0:
    seculo = ano // 100
    print(seculo)
else:
    seculo = (ano // 100) + 1
    print(seculo)