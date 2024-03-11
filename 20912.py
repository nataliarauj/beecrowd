while True:
    n = int(input())
    if n == 0:
        break
    else:     
        numeros = [int(x) for x in input().split()]
        lista = []

        for i in numeros:
            if i in lista:
                lista.remove(i)
            else:
                lista.append(i)
        print(lista[0])

