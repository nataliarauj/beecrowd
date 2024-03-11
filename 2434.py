valores = input().split()
dias, saldo = map(int, valores)
menor_valor = saldo

for i in range(dias):
    saldo_auxiliar = int(input())

    if saldo_auxiliar > 0:
        saldo += saldo_auxiliar
    else:
        saldo_auxiliar 
        saldo = saldo - (saldo_auxiliar * (-1))  

    if saldo < menor_valor:
        menor_valor = saldo

print(menor_valor)