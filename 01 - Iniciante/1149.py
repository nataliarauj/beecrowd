valores = input().split()
a = int(valores[0])
n = int(valores[1])

while n <= 0:
    valores = input().split()
    n = int(valores[1]) 

soma = 0
for i in range(n):
    soma += a
    a += 1

print(soma)