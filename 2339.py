valores = input().split()
competidores, papel_comprado, qtd_papel = map(int, valores)
total = qtd_papel * competidores

if papel_comprado >= total:
    print('S')
else:
    print('N')