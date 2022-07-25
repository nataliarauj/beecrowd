num = int(input())
x = 0
for i in range(1, 100):
    num = int(input())

    if(num>x):
        maior = num
        posicao = i + 1
        x = num

print(maior)
print(posicao)
