horario = input().split()

inicioH, inicioM, fimH, fimM = map(int, horario)

if(inicioH >= fimH):

    formula = 24 - inicioH + fimH
    
    if(inicioM > fimM):
        formula = formula - 1
        formulaM = 60 - (inicioM - fimM)
  
    else:
        formulaM = fimM - inicioM

    if(inicioM != fimM):
        print('O JOGO DUROU 0 HORA(S) E', formulaM, 'MINUTO(S)') 
        exit()


    print('O JOGO DUROU', formula, 'HORA(S) E', formulaM, 'MINUTO(S)')

else:
    formula2 = fimH - inicioH
    
    if(inicioM > fimM):
        formula2 = formula2 - 1
        formulaM = 60 - (inicioM - fimM)
  
    else:
        formulaM = fimM - inicioM
    
    print('O JOGO DUROU', formula2, 'HORA(S) E', formulaM, 'MINUTO(S)')
