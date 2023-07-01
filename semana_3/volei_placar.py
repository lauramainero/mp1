time1 = input()
time2 = input()

pontuacao = [int(p) for p in input().split()]
pontuacao_time1 = pontuacao[0]
pontuacao_time2 = pontuacao[1]
ponto = pontuacao[2]

if ponto == 1:
    pontuacao_time1 += 1
else:
    pontuacao_time2 += 1

if pontuacao_time1 > 23:
    pontuacao_time1 = 23
elif pontuacao_time2 > 23:
    pontuacao_time2 = 23

print(time1, pontuacao_time1)
print(time2, pontuacao_time2)
