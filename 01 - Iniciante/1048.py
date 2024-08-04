salario = float(input())

reajuste = 0
pReajuste = 0

if(salario <= 400.00):
    pReajuste = 15
    reajuste = salario * (pReajuste / 100)
elif(salario >= 400.01 and salario <= 800.00):
    pReajuste = 12
    reajuste = salario * pReajuste
elif(salario >= 800.01 and salario <= 1200.01):
    pReajuste = 10
    reajuste = salario * (pReajuste / 100)
elif(salario >= 1200.01 and salario <= 2000):
    pReajuste = 7
    reajuste = salario * (pReajuste / 100)
else:
    pReajuste = 4
    reajuste = salario * (pReajuste / 100)

novoSalario = reajuste + salario


print('Novo salario: %.2f' % novoSalario)
print('Reajuste ganho: %.2f' % reajuste)
print('Em percentual: {} %'.format(pReajuste))