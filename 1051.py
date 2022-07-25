salario = float(input())

if 0 < salario <= 2000.00:
    print('Isento')

elif 2000.0 < salario <= 3000.00:
    imposto = salario * 0.08

elif 3000.01 < salario <= 4500.00:
    imposto = (1000 * 0.08)
    i18 = salario - 3000
    imposto = (i18 * 0.18) + imposto

else:
    imposto = salario * 0.28

print(f'R$ {imposto:.2f}')