valores = input().split()
c1, c2, c3, c4 = map(int, valores)
lista = [c1, c2, c3, c4]

for p, valor in enumerate(lista): 
    if valor == 1:
        print(p+1)  