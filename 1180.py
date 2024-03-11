
n = int(input())
lista_str = input().split()
lista_int = []
for i in range(0, n):
    for j in lista_str:
        lista_int.append(int(j))

print(f'Menor valor: {min(lista_int)}')
for i in enumerate(lista_int):
    print(f'Posição: {lista_int.index(min(lista_int))}')
    break