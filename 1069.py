qtd = int(input())

for i in range(qtd):
    mineracao = input().strip()
    diamantes = 0
    armazenamento_diamantes = list()

    for c in mineracao:
        if '<' == c:
            armazenamento_diamantes.append(c)
        elif '>' == c and len(armazenamento_diamantes):
            armazenamento_diamantes.append(c)
            diamantes += 1
    print(diamantes)