"""For / Else em Python"""

#break and continue ainda existem no for

variavel=['luiz', 'th', 'guerra']
comecacomt=False
for valor in variavel:
    print(valor)
    if valor.startswith('t'): #startswith() confere se a string começa com oq for passado
        comecacomt=True
if comecacomt: 
    print('tem alguma palavra que começa com t')
else: 
    print('não tem uma palavra que começa com t')