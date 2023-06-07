banco = int(input())
carrinho = int(input())
saldo = banco - carrinho
if banco >= carrinho:
    print("se você comprar tudo o saldo será: " + str(saldo))
else:
    print("seu saldo é insuficiente para essa compra")