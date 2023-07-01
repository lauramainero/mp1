# entrada: 
    # primeira linha: uma palavra simples (sem espaços)
    # linhas seguintes: uma letra por linha
    # ultima linha: um ponto final
# saida: true ou false

palavra = input()
soletrado = ''

while True:
    letra = input()

    if letra != '.':
        soletrado += letra

    if letra == '.':
        break
    
if soletrado == palavra:
    print('True')
else:
    print('False')