n = int(input())

if n % 2 == 0:
    for j in range(1,12,2):
        print(j+n)

else:
    for i in range(n,n+12, 2):
        print(i)