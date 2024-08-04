values1 = input().split()
values2 = input().split()

cod1, n1, val1 = map(float, values1)
cod2, n2, val2 = map(float, values2)

saida = n1 * val1 + n2 * val2

print('VALOR A PAGAR: R$ %.2f' % saida)