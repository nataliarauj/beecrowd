values = input().split()

a, b, c = map(float, values)

triangulo = (a * c) / 2
circulo = 3.14159 * (c * c)
trapezio = (a + b) / 2 * c
quadrado = b * b
retangulo = a * b

print('TRIANGULO: %.3f' % triangulo + 
'\nCIRCULO: %.3f' % circulo +
'\nTRAPEZIO: %.3f' % trapezio + 
'\nQUADRADO: %.3f' % quadrado +
'\nRETANGULO: %.3f' % retangulo)
