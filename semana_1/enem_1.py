# notas em cada disciplina
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
nota4 = int(input())
nota5 = int(input())

# pesos de cada disciplina
peso1 = int(input())
peso2 = int(input())
peso3 = int(input())
peso4 = int(input())
peso5 = int(input())

# soma das notas multiplicadas pelos seus respectivos pesos
soma_notas = nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4 + nota5 * peso5

# soma dos pesos
soma_pesos = peso1 + peso2 + peso3 + peso4 + peso5

# calculo e impressao da media total
media = soma_notas / soma_pesos
print(media)