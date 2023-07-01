n_min = int(input())

n_soma = 0

while n_soma < n_min:
    min_atingido = False
    n = int(input())
    n_soma += n

    if n_soma >= n_min:
        min_atingido = True

        n_sobra = n_soma - n_min

        print('minimo', n_min)
        print('total', n_soma)
        print('sobra', n_sobra)