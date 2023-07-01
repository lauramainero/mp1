cpf = input()

cpf = cpf.replace('-', '').replace('.', '')

if len(cpf) != 11:
    print('ERROR')
else:
    print('OK')

