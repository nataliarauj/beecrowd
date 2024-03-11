c = int(input())
while c > 0:
    n = int(input())
    numeros = list()

    for i in range(n):
        if i % 2 == 0:
            numeros.append(1)
        else:
            numeros.append(-1)
    
    print(sum(numeros))
    c -=1