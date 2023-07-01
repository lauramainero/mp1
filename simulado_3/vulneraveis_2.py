idade = int(input())

mensagem = ''

if idade < 10:
    mensagem = 'De acordo com especialistas, é contraindicado o acesso às mídias sociais e telas na sua faixa etária'
elif 10 < idade <= 12:
    mensagem = 'De acordo com especialistas, é contraindicado o acesso às mídias sociais e telas na sua faixa etária.\nSua idade coloca você entre as jovens mais vulneráveis: jovens de 10 a 12 anos'
else:
    mensagem = 'Usar as telas ou computadores não é o problema, mas sim como fazemos uso dessas ferramentas'

print(mensagem)
