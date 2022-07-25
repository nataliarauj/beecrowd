ageDays = int(input())

anos = ageDays // 365
ageDays = ageDays - anos * 365

meses = ageDays // 30
ageDays = ageDays - meses * 30

dias = ageDays

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))