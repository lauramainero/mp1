operacao = input()
num1 = int(input())
num2 = int(input())
if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
elif operacao == '//':
    print(num1 // num2)
elif operacao == '%':
    print(num1 % num2)
else:
    print(num1 ** num2)