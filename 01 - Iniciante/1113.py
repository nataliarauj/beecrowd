x = 0
y = 1

while x != y:
    valores = input().split()
    x, y = map(int, valores)
    if x > y:
        print('Decrescente')
    elif y > x:
        print('Crescente')