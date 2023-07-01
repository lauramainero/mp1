cpf = input()

if '-' in cpf or '.' in cpf:
    cpf = cpf.replace('-', '').replace('.', '')
    print(cpf)
else:
    print(cpf)