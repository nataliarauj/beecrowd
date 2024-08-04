idade = int(input())

total = 0
repeat = 0

while(idade > 0):
    repeat += 1
    total += idade
    media = total / repeat

    if idade < 0:
        break

    idade = int(input())

print('%.2f' % media)
