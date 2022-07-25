n = int(input())

pretas = (n ** 2) // 2

if n % 2 == 0:
    brancas = pretas
else:
    brancas = pretas + 1

print('{:.0f} casas brancas e {:.0f} casas pretas'.format(brancas, pretas))