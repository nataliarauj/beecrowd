valores = input().split()

cod, qtd = map(int, valores)

total = 0

if cod == 1:
    preco = 4.0
    total = preco * qtd
    print('Total: R$ %.2f' % total)

elif cod == 2:
    preco = 4.50
    total = preco * qtd
    print('Total: R$ %.2f' % total)

elif cod == 3:
    preco = 5.0
    total = preco * qtd
    print('Total: R$ %.2f' % total)

elif cod == 4:
    preco = 2.0
    total = preco * qtd
    print('Total: R$ %.2f' % total)

elif cod == 5:
    preco = 1.50
    total = preco * qtd
    print('Total: R$ %.2f' % total)