numero_testes = int(input())

for i in range(numero_testes):
    teste = int(input())

    primo = True

    for c in range(2, teste):
        if teste % c == 0:
            primo = False
            break

    if primo:
        print('{}eh primo'.format(teste))

    else:
        print('{} nao eh primo'.format(teste))

        
