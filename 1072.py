n = int(input())

inside = 0
out = 0

for i in range(0, n):
    valores = int(input())

    if valores in range(10, 21):
        inside += 1
    else:
        out += 1

print(f'{inside} in')
print(f'{out} out')