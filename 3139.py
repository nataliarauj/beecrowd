associacao = input().split()
seguidores, necessario = map(int, associacao)

ideal = necessario - seguidores
print(ideal)