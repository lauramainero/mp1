caractere = input()
if caractere in 'aeiouAEIOU':
    print("vogal")
elif caractere in '@#$%&*()_-+=!':
    print("especial")
elif caractere in '1234567890':
    print("algarismo")
else:
    print("outro")