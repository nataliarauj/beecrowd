total_cobaias = total_coelhos = total_sapos = total_ratos = 0
perc_coelhos = perc_ratos = perc_sapos = 0
num_casos = int(input())


for i in range(1, num_casos+1):
    cobaias = input().split()
    num_cobaia, tipo_cobaia = map(str, cobaias)
    num_cobaia_convertido = int(num_cobaia)

    total_cobaias += num_cobaia_convertido

    if tipo_cobaia == 'S':
        total_sapos += num_cobaia_convertido
    elif tipo_cobaia == 'C':
        total_coelhos += num_cobaia_convertido
    elif tipo_cobaia == 'R':
        total_ratos += num_cobaia_convertido

    perc_coelhos = (total_coelhos * 100) / total_cobaias
    perc_ratos = (total_ratos * 100) / total_cobaias
    perc_sapos = (total_sapos * 100) / total_cobaias


print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {perc_coelhos:.2f} %')
print(f'Percentual de ratos: {perc_ratos:.2f} %')
print(f'Percentual de sapos: {perc_sapos:.2f} %')
