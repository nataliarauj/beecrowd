valores = input().split()
m, n = map(int, valores)

for i in range(n):
    option = input()

    if option.upper() == 'FECHOU':
        m += 1
    elif option.upper() == 'CLICOU':
        m -= 1
print(m)
