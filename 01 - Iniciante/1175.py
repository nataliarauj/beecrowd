a = []

for i in range(4):
    v = int(input())
    a.append(v)

v = a[::-1]

for s in range(4):
    print('N[{}] = {}'.format(s, v[s]))

