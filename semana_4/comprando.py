saldo = float(input())

itens = []

while saldo >= 0:
    valor_do_item = float(input())
    saldo -= valor_do_item
    
    if saldo >= 0:
        itens.append(valor_do_item)

saldo += valor_do_item

print('Número de itens', len(itens))
print('Saldo: %.2f' % saldo)
