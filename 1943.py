colocacao = int(input())

if colocacao == 1:
    print('Top 1')
elif 2 <= colocacao <= 3:
    print('Top 3')
elif 4 <= colocacao <= 5:
    print('Top 5')
elif 6 <= colocacao <= 10:
    print('Top 10')
elif 11 <= colocacao <= 25:
    print('Top 25')
elif 26 <= colocacao <= 50:
    print('Top 50')
else:
    print('Top 100')