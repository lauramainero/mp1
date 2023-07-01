num_votos = int(input())

votos = [ ]

for _ in range(num_votos):
    v = input()
    votos.append(v)

x = [ ]
y = [ ]
b_n = [ ]

for v in votos:
    if v == 'X':
        x.append(v)
    elif v == 'Y':
        y.append(v)
    elif v == 'B' or v == 'N':
        b_n.append(v)
    
print('X', len(x))
print('Y', len(y))
print('Brancos e nulos', len(b_n))

if len(x) > len(y):
    print('vitoria: X')
elif len(y) > len(x):
    print('vitoria: Y')
else:
    print('empate!')