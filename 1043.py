valores = input().split()

a, b,c = map(float, valores)

if(a < b + c and abs(b -c) < a):
    perimetro = a + b + c
    print('Perimetro = %.1f' % perimetro)

else:
    area = (a + b) * c / 2
    print('Area = %.1f' % area)

