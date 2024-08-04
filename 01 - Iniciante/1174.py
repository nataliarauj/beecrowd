a = []

for i in range(0, 101):
    v = float(input())
    a.append(v)

    if v <= 10.0:
        print('A[{}] = {}'.format(i, v))
