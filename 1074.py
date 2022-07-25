num = int(input())

for i in range(0, num):
    n = int(input())

    if n % 2 == 0 and n > 0:
        print('EVEN POSITIVE')
    elif n % 2 == 0 and n < 0:
        print( 'EVEN NEGATIVE')

    if n % 2 != 0 and n > 0:
        print( 'ODD POSITIVE')
    elif n % 2 != 0 and n < 0:
        print('ODD NEGATIVE')

    elif n == 0:
        print('NULL')