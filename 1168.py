#0,1,2,3,4,5,6,7,8,9
leds = [6,2,5,5,4,5,6,3,7,6]

qtd = int(input())

for i in range(qtd):
    total_leds = 0
    n = input()
    map(int, n)
    
    for j in range(len(n)):
        ind = int(n[j])
        total_leds += leds[ind]

    print(f"{total_leds} leds")