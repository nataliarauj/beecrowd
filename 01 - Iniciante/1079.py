vzs = int(input())

for i in range(0, vzs):
    notas = input().split()
    n1, n2, n3 = map(float, notas)

    media1 = (((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10)

    print(f'{media1:.1f}')
