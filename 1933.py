cartas_recebidas = input().split()
c1, c2 = map(int, cartas_recebidas)

ultima_carta = 0

if c1 != c2:
    if c1 > c2:
        ultima_carta = c1
    elif c2 > c1:
        ultima_carta = c2
    
elif c1 == c2:
    ultima_carta = c1

print(ultima_carta)