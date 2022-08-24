"""
criar contadores usando laços de repetição
contador 1: 0 1 2 3 4 5 6 7 8 
contador 2: 10 9 8 7 6 5 4 3 2
"""
#meu código
cont1=0
cont2=10
z = True
while z:
    print(f'Contador 1: {cont1} Contador 2: {cont2}')
    cont1=cont1+1
    cont2-=1
    if cont1>8:
        break
#código do professor
for p,r in enumerate(range(10,1,-1)):
    print(p,r)

