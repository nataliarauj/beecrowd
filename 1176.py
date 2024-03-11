t = int(input())

for i in range(t):
    fib = int(input())

    f = 1
    for c in range(fib):
        f *= c
        print(f'Fib({fib}) = {f}')