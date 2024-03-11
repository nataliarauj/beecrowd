numero = int(input()) 

if numero < 10000:
    for i in range(0, 10000+1):
        if i % numero == 2:
            print(i)
