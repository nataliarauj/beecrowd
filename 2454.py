posicoes = input().split()
p, r = map(int, posicoes)

if p == 0 and r == 1:
    caminho = 'C'
if p == 1 and r == 0:
    caminho = 'B'
if p == 1 and r == 1:
    caminho = 'A'
if p == 0 and r == 0:
    caminho = 'C'

print(caminho)