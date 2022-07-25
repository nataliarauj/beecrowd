horario = input().split()

inicio, fim = map(int, horario)

if(inicio >= fim):
    formula = 24 - inicio + fim
    print('O JOGO DUROU', formula, 'HORA(S)')

else:
    formula2 = fim - inicio
    print('O JOGO DUROU', formula2, 'HORA(S)')
