
positivos = 0
soma = 0
for i in range (0,6):
    n = float(input())

    if n > 0:
        positivos += 1
        soma = soma + n
        

    media = soma / positivos
    

print('{} valores positivos'.format(positivos))
print('{:.1f}'.format(media))

