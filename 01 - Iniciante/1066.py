par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(0, 5):
    n = int(input())

    if n > 0:
        positivo += 1
    
    elif n <0:
        negativo += 1
    
    if n % 2 == 0:
        par += 1
    elif n % 2 != 0:
        impar += 1
    
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))