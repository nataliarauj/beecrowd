
values1 = input().split()

a, b, c = map(float, values1)


delta = (b ** 2) - (4 * a * c)

if (a == 0.0 or delta < 0.0):
    print('Impossivel calcular')

else:
    calculo1 = (- b + (delta ** (0.5))) / (2 * a)
    calculo2 = (- b - (delta ** (0.5))) / (2 * a)
    print('R1 = %.5f' % calculo1)
    print('R2 = %.5f' % calculo2)
