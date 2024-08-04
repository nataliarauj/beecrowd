notas = input().split()

n1, n2, n3, n4 = map(float, notas)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10


if(media >= 7.0):
    print('Media: %.1f' % media)
    print('Aluno aprovado.')

elif(media < 5.0):
    print('Media: %.1f' % media)
    print('Aluno reprovado.')

elif(media >= 5.0 and media <= 6.9):
    print('Media: %.1f' % media)
    print('Aluno em exame.')

    notaExame = float(input())

    print('Nota do exame:', notaExame)
    media2 = (notaExame + media) / 2

    if(media2 >= 5):
        print('Aluno aprovado.')
        print('Media final:', media2)
    else:
        print('Aluno reprovado.')
        print('Media final:', media2)
