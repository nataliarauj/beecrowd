grenal_cont = 0
continuar = 0
cont_empates = 0
vitorias_inter = 0
vitorias_gremio = 0

while True:
    gols = input().split()
    inter, gremio = map(int, gols)
    print("Novo grenal (1-sim 2-nao)")
    continuar = int(input())
    grenal_cont +=1

    if gremio == inter:
        cont_empates += 1
    elif gremio > inter:
        vitorias_gremio += 1
    elif inter > gremio:
        vitorias_inter += 1
    
    if continuar == 2:
        break 
        
    
print(f"{grenal_cont} grenais")
print(f"Inter:{vitorias_inter}")
print(f"Gremio:{vitorias_gremio}")
print(f"Empates:{cont_empates}")

if gremio > inter:
    print("Gremio ganhou mais")
elif inter > gremio:
    print("Inter ganhou mais")
else:
    print("Nao houve vencedor")