n = int(input())

for _ in range(n):
    valores = input().split()
    x, y = map(int, valores)
    numeros = []

    if x > y:
        for i in range (x - 1, y, -1):
            if i % 2 != 0:
                numeros.append(i)

    if y > x:
        for j in range (y - 1, x, -1):
            if j % 2 != 0:
                numeros.append(j)
    print(sum(numeros))