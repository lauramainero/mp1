total = [] # minimo total de 200 com 50 em cada semana

l1 = total.append(int(input()))
l2 = total.append(int(input()))
l3 = total.append(int(input()))
l4 = total.append(int(input()))

resultado = ''

if 100 > total[0] >= 50 and 100 > total[1] >= 50 and 100 > total[2] >= 50 and 100 > total[3] >= 50:
    resultado = 'Certificado Meninas Programadoras'
elif total[0] >= 100 and total[1] >= 100 and total[2] >= 100 and total[3] >= 100:
    resultado = 'Certificado Meninas Programadoras + Selo 100 de Prática'
elif total[0] >= 50 and total[1] >= 50 and total[2] >= 50 and total[3] >= 50 and sum(total) >= 200:
    resultado = 'Certificado Meninas Programadoras'
else:
    resultado = 'Mínimo de prática não alcançado'

print(resultado)