qtd_intervalos = int(input())
soma = 0
for i in range(qtd_intervalos):
    valores = input().split()
    t, v = map(int, valores)

    distancia_total = v * t
    soma += distancia_total
print(soma)