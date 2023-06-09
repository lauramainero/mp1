idade1 = int(input())
idade2 = int(input())
idade3 = int(input())
idade4 = int(input())
if idade1 > idade2 and idade1 > idade3 and idade1 > idade4:
    print("A mais velha tem " + str(idade1) + " anos")
elif idade2 > idade1 and idade2 > idade3 and idade2 > idade4:
    print("A mais velha tem " + str(idade2) + " anos")
elif idade3 > idade1 and idade3 > idade2 and idade3 > idade4:
    print("A mais velha tem " + str(idade3) + " anos")
else:
    print("A mais velha tem " + str(idade4) + " anos")