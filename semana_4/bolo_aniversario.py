# entrada: uma linha com o numero de velinhas do bolo
# loop: numero indeterminado de entradas com onomatopeia que indique um sopro
# saida: indicação da força dos sopros e mensagem de feliz aniversario ao apagar todas as velinhas

n_velas = int(input())

idade = 0

while n_velas > 0:
    sopro = input()

    if len(sopro) < 4:
        print('precisa de muito mais força no sopro!')
    elif 4 <= len(sopro) < 8:
        print('um pouco mais de força no sopro!')
    elif len(sopro) >= 8:
        print('bom sopro!')
        n_velas -= 1
        idade += 1

        if n_velas == 0:
            break
print('Ariel, parabéns pelo seu aniversário de', idade, 'anos!')

    