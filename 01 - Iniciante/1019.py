n = int(input())

horas = n // 3600
resto = n % 3600

minu = resto // 60

seg = resto % 60

print('{:.0f}:{:.0f}:{:.0f}'.format(horas, minu, seg))