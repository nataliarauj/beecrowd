amigos = list()
nao_amigos = list()
todos = list()
maior = ''

while True:
    try:
        inscricao = input().split()
        nome, amigo = map(str, inscricao)

        if amigo == "YES" and nome not in amigos:
            amigos.append(nome)
        elif amigo == "NO" and nome not in nao_amigos:
            nao_amigos.append(nome)
        if nome == "FIM":
           break
    except:
        break

todos = sorted(amigos) + sorted(nao_amigos)
maior = 0
for i in range(len(amigos)):
    if len(amigos[i]) > len(amigos[maior]):
        maior = i
    elif len(amigos[i]) == len(amigos[maior]):
        if i < maior:
            maior = i

for c in todos:
    print(c)
print('')

print('Amigo do Habay:')
print(amigos[maior])