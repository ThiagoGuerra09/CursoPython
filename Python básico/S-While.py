"""Repetiçaõ com while"""
x=0
while x<=10: #contador até 10
    if x ==3:
        x=x+1
        continue # continue, faz ele voltar para o loop e consequentemente não vai realizar oq ta embaixo, logo não printou o 3
    print(x)
    x = x + 1 

x=0
while x<=10: #contador até 10
    if x ==3:
        x=x+1
        break # quando ele encontra o break ele sai/quebra do loop
    print(x)
    x = x + 1 #x+=1 é a msm coisa

print('acabou')

#exercicio criando coordenadas 
x=0
while x<5:
    y=0
    while y<5:
        print(f'({x},{y})')
        y +=1
    x+=1
    
