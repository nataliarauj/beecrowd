x = y = 1

while x != 0 and y != 0:
    coordenadas = input().split()
    x, y = map(int, coordenadas)
    if x > 0:
        if y > 0:
            print('primeiro')
        if y < 0:
            print('quarto')
    if x < 0:
        if y > 0:
            print('segundo')
        if y < 0:
            print('terceiro')

