x = []

for i in range(0,5):
    x.append(int(input()))

for c in range(0,5):
    if (x[c] <= 0):
        x[c] = 1 
    print('X[{}] ='.format(c), x[c])