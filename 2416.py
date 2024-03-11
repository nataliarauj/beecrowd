valores = input().split()
pretensao_corrida, comprimento_pista = map(int, valores)

termino = pretensao_corrida % comprimento_pista
print(termino)