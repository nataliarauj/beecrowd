qtd_produtos = int(input())
total_pedido = 0

for i in range(qtd_produtos):
    pedido = input().split()
    cod, qtd = map(int, pedido)

    if cod == 1001:
        total_pedido += 1.50 * qtd
    elif cod == 1002:
        total_pedido += 2.50 * qtd
    elif cod == 1003:
        total_pedido += 3.50 * qtd
    elif cod == 1004:
        total_pedido += 4.50 * qtd
    elif cod == 1005:
        total_pedido += 5.50 * qtd

print(f'{total_pedido:.2f}')