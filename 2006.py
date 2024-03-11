t = int(input())
correto = 0

resposta_competidores = input().split()
c1, c2, c3, c4, c5 = map(int, resposta_competidores)


if c1 == t:
    correto += 1
if c2 == t:
    correto += 1
if c3 == t:
    correto += 1
if c4 == t:
    correto += 1
if c5 == t:
    correto +=1

print(correto)