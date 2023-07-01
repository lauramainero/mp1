cpf = input()

cpf = cpf.replace('-', '').replace('.', '')

if not cpf.isnumeric():
    print('ENCODING ERROR')
if len(cpf) != 11:
    print('SIZE ERROR')
if cpf.isnumeric() and len(cpf) == 11:
    print(cpf)