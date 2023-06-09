idade1 = int(input())
idade2 = int(input())
idade3 = int(input())
idade4 = int(input())
if idade1 > (idade2 and idade3 and idade4) and idade2 < (idade1 and idade3 and idade4):
    print("A mais velha tem " + str(idade1))
    print("A mais nova tem " + str(idade2))
elif idade1 > (idade2 and idade3 and idade4) and idade3 < (idade1 and idade2 and idade4):
    print("A mais velha tem " + str(idade1))
    print("A mais nova tem " + str(idade3))
elif idade1 > (idade2 and idade3 and idade4) and idade4 < (idade1 and idade2 and idade3):
    print("A mais velha tem " + str(idade1))
    print("A mais nova tem " + str(idade4))
elif idade2 > (idade1 and idade3 and idade4) and idade1 < (idade2 and idade3 and idade4):
    print("A mais velha tem " + str(idade2))
    print("A mais nova tem " + str(idade1))
elif idade2 > (idade1 and idade3 and idade4) and idade3 < (idade1 and idade2 and idade4):
    print("A mais velha tem " + str(idade2))
    print("A mais nova tem " + str(idade3))
elif idade2 > (idade1 and idade3 and idade4) and idade4 < (idade1 and idade2 and idade3):
    print("A mais velha tem " + str(idade2))
    print("A mais nova tem " + str(idade4))
elif idade3 > (idade1 and idade2 and idade4) and idade1 < (idade2 and idade3 and idade4):
    print("A mais velha tem " + str(idade3))
    print("A mais nova tem " + str(idade1))
elif idade3 > (idade1 and idade2 and idade4) and idade2 < (idade1 and idade3 and idade4):
    print("A mais velha tem " + str(idade3))
    print("A mais nova tem " + str(idade2))
elif idade3 > (idade1 and idade2 and idade4) and idade4 < (idade1 and idade2 and idade3):
    print("A mais velha tem " + str(idade3))
    print("A mais nova tem " + str(idade4))
elif idade4 > (idade1 and idade2 and idade3) and idade1 < (idade2 and idade3 and idade4):
    print("A mais velha tem " + str(idade4))
    print("A mais nova tem " + str(idade1))
elif idade4 > (idade1 and idade2 and idade3) and idade2 < (idade1 and idade3 and idade4):
    print("A mais velha tem " + str(idade4))
    print("A mais nova tem " + str(idade2))
else:
    print("A mais velha tem " + str(idade4))
    print("A mais nova tem " + str(idade3))