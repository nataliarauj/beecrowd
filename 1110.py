#Autores: Cícero Breno de Lima Alves e Francisca Natália Silvestre Araújo
#Loop infinito para receber as cartas, quando o usuário digitar 0
#o código para.
while True:
    n = int(input())
    if n == 0:
        break

    #Duas listas vazias são criadas
    cartas = []
    descartadas = [] 
    #O loop abaixo adiciona os valores de 1 a n na lista "cartas"
    for i in range(n):
        cartas.append(i+1)
    #Enquanto o número de cartas for maior que 2, a primeira carta é removida
    #e adicionada na lista de descartadas. E a segunda carta é movida para o fim da lista "cartas"
    while len(cartas) >= 2:
        descartadas.append(cartas.pop(0))
        cartas.append(cartas.pop(0))

    #As cartas descartadas são mostradas em linha separadas com vírgula
    #sendo formatadas usando o método for
    print(f'Discarded cards: ', end='')
    for c in descartadas[:-1]:
        print(f'{c}', end=', ')
    print(descartadas[-1])
    #A carta que sobrou é mostrada em outra linha, também sendo formatada
    print('Remaining card: ', end='')
    for j in cartas:
        print(f'{j}')