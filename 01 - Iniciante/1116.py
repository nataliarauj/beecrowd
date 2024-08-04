num_teste = int(input())

for i in range(0,num_teste):
    valores = input().split()
    x, y = map(int, valores)
    
    if y == 0:
        print('divisao impossivel')
    else:
        div = x / y
        print(f'{div:.1f}')