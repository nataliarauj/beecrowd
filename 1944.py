qtd = int(input())
letras = ['F', 'A', 'C', 'E']

for i in range(qtd):
    letras_input = input().split()
    letras_separadas = list(letras_input)
    letras.append(letras_separadas)



    

print(letras)