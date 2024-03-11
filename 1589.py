num_teste = int(input())
menor_raio = 0
for i in range(num_teste):
    raios = input().split()
    r1, r2 = map(int, raios)

    menor_raio = r1 + r2
    print(menor_raio)