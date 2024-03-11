qtd_porcoes = list()
porcoes = [300, 1500, 600, 1000, 150]
soma = 225

for i in range(5):
    p = int(input())
    qtd_porcoes.append(p)
    
for j, k in zip(qtd_porcoes, porcoes):
    total = j * k
    soma += total
print(soma)