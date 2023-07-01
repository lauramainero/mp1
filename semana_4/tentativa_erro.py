n_alvo = int(input())

chutes = []
n_chute = 0
palpite = ''

while True:
    n_chute = int(input())

    if n_chute == n_alvo:
        palpite = 'igual'
        chutes.append(palpite)
        break
    elif n_chute > n_alvo:
        palpite = 'menor'
        chutes.append(palpite)
        continue
    elif n_chute < n_alvo:
        palpite = 'maior'
        chutes.append(palpite)
        continue

for c in chutes:
    print(c)