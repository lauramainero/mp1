# entrada: um conjunto indeterminado de requisicoes de memória:
    # - um valor positivo corresponde a uma requisição de memoria
    # - um valor negativo corresponde a uma liberação de memória
    # - um valor nulo encerra a entrada de dados
# saida: o maior valor de memória utilizada durante toda a execução do programa.

memoria_atual = 0
memoria_max = 0

while True:
    valor = int(input())

    memoria_atual += valor

    if valor == 0:
        break

    if memoria_atual > memoria_max:
        memoria_max = memoria_atual
print(memoria_max)