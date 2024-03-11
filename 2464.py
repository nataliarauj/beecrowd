alfa = {}
alfa2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
seq = input()
cripto = input()

#Transforma a palavra em lista com as letras separadas
sep = list(seq)
cripto_sep = list(cripto)
traducao = []

#Troca as letras pela permutação inreversível
for letra in range(len(sep)):
    alfa[alfa2[letra]] = sep[letra]

for l in cripto_sep:
    traducao.append(alfa[l])

print("".join(traducao))