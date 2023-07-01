placa = int(input())
digito = placa % 10
if digito == 1 or digito == 2:
    print("segunda-feira")
elif digito == 3 or digito == 4:
    print("terça-feira")
elif digito == 5 or digito == 6:
    print("quarta-feira")
elif digito == 7 or digito == 8:
    print("quinta-feira")
else:
    print("sexta-feira")

