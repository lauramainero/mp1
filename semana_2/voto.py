idade = int(input())
if idade == 16 or idade == 17 or idade >= 70:
    print("Seu voto é facultativo: você pode votar ou não")
elif 16 < idade < 70:
    print("Seu voto é obrigatório")
else:
    print("Jovem demais para votar, espere até 16")