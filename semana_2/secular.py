ano = int(input())
if ano <= 100:
    print("1")
else:
    seculo = (ano // 100) + 1
    print(seculo)