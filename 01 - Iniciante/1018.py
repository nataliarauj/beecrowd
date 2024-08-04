n = int(input())
n2 = n

nota_cem = n / 100
n = n % 100

nota_cinquenta = n / 50
n = n % 50

nota_vinte = n / 20
n = n % 20

nota_dez = n / 10
n = n % 10

nota_cinco = n / 5
n = n % 5

nota_dois = n / 2
n = n % 2

nota_um = n / 1
n = n % 1

print(n2)
print("%d nota(s) de R$ 100,00" %nota_cem)
print("%d nota(s) de R$ 50,00" %nota_cinquenta)
print("%d nota(s) de R$ 20,00" %nota_vinte)
print("%d nota(s) de R$ 10,00" %nota_dez)
print("%d nota(s) de R$ 5,00" %nota_cinco)
print("%d nota(s) de R$ 2,00" %nota_dois)
print("%d nota(s) de R$ 1,00" %nota_um)