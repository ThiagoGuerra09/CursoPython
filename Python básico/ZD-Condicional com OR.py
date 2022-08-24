"""
Condição com OR
"""

nome = input('digite seu nome')

# nome=nome if nome else 'Voce não digitou nada'
# print(nome)

#ainda podemos reduzir mais ainda usando o OR
print(nome or 'vocee não digitou nada')#confere se nome for True ele executa a primeira, se for false ele printa a segunda
#lembrando que o OR para no primeiro True que encontra