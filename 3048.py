tam_seq = int(input())
sequencia = []

for i in range(tam_seq):
    n = int(input())
    
    if not sequencia:
        sequencia.append(n)
    elif n != sequencia[-1]:
        sequencia.append(n)
    
print(len(sequencia))