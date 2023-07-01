idade1 = int(input())
idade2 = int(input())
idade3 = int(input())
idade4 = int(input())

if idade1 > idade2:
    maior = idade1
    menor = idade2
else:
    maior = idade2
    menor = idade1

if idade3 > maior:
    maior = idade3
else:
    menor = idade3

if idade4 > maior:
    maior = idade4
else:
    menor = idade4

print("A mais velha tem " + str(maior))
print("A mais nova tem " + str(menor))