area_abertura = int(input())
num_estrelas = int(input())

estrelas_percebidas = 0

for _ in range(num_estrelas):
    fluxo_fotons = int(input())
    
    if fluxo_fotons * area_abertura >= 40000000:
        estrelas_percebidas += 1

print(estrelas_percebidas)