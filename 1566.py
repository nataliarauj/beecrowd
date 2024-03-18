#Aluna: Francisca Natália Silvestre Araújo
import sys
qtd_testes = int(sys.stdin.readline())

for i in range(qtd_testes):
    qtd_pessoas = int(sys.stdin.readline())
    alturas = list(map(int, sys.stdin.readline().split()))

    alturas.sort()
    print(" ".join(map(str, alturas)))