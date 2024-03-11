while True:
    valores = input().split()
    x, m = map(int, valores)
    if x == 0 and m == 0:
        break

    new_xp = m * x
    print(new_xp)