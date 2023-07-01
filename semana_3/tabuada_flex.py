num = int(input())
f_num = int(input())
l_num = int(input())

print('Tabuada do', num, 'de', f_num, 'até', l_num)

for n in range(f_num, l_num + 1):
    resultado = num * f_num
    print(num, 'x', n, '=', resultado)
    f_num += 1