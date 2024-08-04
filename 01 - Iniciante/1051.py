salario = float(input())
imposto = 0

if salario <= 2000.00:
    print('Isento')
else:
    if 2000.00 < salario <= 3000.00:
        # Aplica 8% sobre a parte do salário que excede R$ 2000.00
        imposto = (salario - 2000.00) * 0.08

    elif 3000.00 < salario <= 4500.00:
        # Aplica 8% sobre a faixa de 2000.01 a 3000.00
        imposto = 1000.00 * 0.08
        # Aplica 18% sobre a parte do salário que excede R$ 3000.00
        imposto += (salario - 3000.00) * 0.18

    elif salario > 4500.00:
        # Aplica 8% sobre a faixa de 2000.01 a 3000.00
        imposto = 1000.00 * 0.08
        # Aplica 18% sobre a faixa de 3000.01 a 4500.00
        imposto += 1500.00 * 0.18
        # Aplica 28% sobre a parte do salário que excede R$ 4500.00
        imposto += (salario - 4500.00) * 0.28
    print(f'R$ {imposto:.2f}')