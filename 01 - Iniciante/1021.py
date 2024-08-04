dinheiro = float(input())

#
nota_cem = dinheiro // 100
dinheiro = dinheiro  % 100

nota_cinquenta = dinheiro // 50
dinheiro = dinheiro % 50

nota_vinte = dinheiro // 20
dinheiro = dinheiro % 20

nota_dez = dinheiro // 10
dinheiro = dinheiro % 10

nota_cinco = dinheiro // 5
dinheiro = dinheiro % 5

nota_dois = dinheiro // 2
dinheiro = dinheiro % 2

#Moedas
moeda1 = dinheiro // 1
dinheiro = dinheiro % 1

moeda50 = dinheiro // 0.50
dinheiro = dinheiro % 0.50

moeda25 = dinheiro // 0.25
dinheiro = dinheiro % 0.25

moeda10 = dinheiro // 0.10
dinheiro = dinheiro % 0.10

moeda5 = dinheiro // 0.05
dinheiro = dinheiro % 0.05

moeda01 = dinheiro / 0.01

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(nota_cem))
print('{:.0f} nota(s) de R$ 50.00'.format(nota_cinquenta))
print('{:.0f} nota(s) de R$ 20.00'.format(nota_vinte))
print('{:.0f} nota(s) de R$ 10.00'.format(nota_dez))
print('{:.0f} nota(s) de R$ 5.00'.format(nota_cinco))
print('{:.0f} nota(s) de R$ 2.00'.format(nota_dois))


print('MOEDAS:')
print(f'{moeda1:.0f} moeda(s) de R$ 1.00')
print(f'{moeda50:.0f} moeda(s) de R$ 0.50')
print(f'{moeda25:.0f} moeda(s) de R$ 0.25')
print(f'{moeda10:.0f} moeda(s) de R$ 0.10')
print(f'{moeda5:.0f} moeda(s) de R$ 0.05')
print(f'{moeda01:.0f} moeda(s) de R$ 0.01')