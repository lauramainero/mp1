peso = float(input())
altura = float(input())

imc = peso / altura ** 2

situacao = ''

if imc < 17:
    situacao = 'Muito abaixo do peso'
elif 17 <= imc <= 18.49:
    situacao = 'Abaixo do peso'
elif 18.50 <= imc <= 24.99:
    situacao = 'Peso normal'
elif 25 <= imc <= 29.99:
    situacao = 'Acima do peso'
elif 30 <= imc < 34.99:
    situacao = 'Obesidade I'
elif 35 <= imc <= 39.99:
    situacao = 'Obesidade II (severa)'
else:
    situacao = 'Obesidade III (mórbida)'

print('%.2f' % imc, situacao)