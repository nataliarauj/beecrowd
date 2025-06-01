while True:
    notas_validas = []
    
    while len(notas_validas) < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notas_validas.append(nota)
        else:
            print("nota invalida")
    
    media = sum(notas_validas) / 2
    print(f"media = {media:.2f}")
    
    while True:
        print("novo calculo (1-sim 2-nao)")
        op = int(input())
        if op == 1:
            break 
        elif op == 2:
            exit(0)  
