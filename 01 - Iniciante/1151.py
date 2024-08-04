n =int(input())
i = 0
l=[]
while i < n:
    if i == 0 or i == 1:
        l.append(i)
     
    if i > 1:
        aux = l[i-2] +l[i-1]
      
        l.append(aux)
    i = i + 1
for j in range(0, n):
    l[j] =str(l[j])
  
l = ' '.join(l)
print(l)