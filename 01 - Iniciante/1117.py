media = 0
while True:
    nota = float(input())

    if 0 < nota > 10:
        print('nota inválida')
    else:
        nota += nota
        media = nota / 2

    print(f'media = {media}')

