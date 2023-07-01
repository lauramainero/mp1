alunas = int(input())

resultados = []

for aluna in range(alunas):
    nome = input()
    s1 = int(input())
    s2 = int(input())
    s3 = int(input())
    s4 = int(input())

    if s1 >= 120 and s2 >= 120 and s3 >= 120 and s4 >= 120:
        resultado = 'tem monitorias OK! :-)'
    else:
        resultado = 'não tem monitorias suficientes :-('

    resultados.append((nome, resultado))

for r in resultados:
    print(r[0], r[1])
