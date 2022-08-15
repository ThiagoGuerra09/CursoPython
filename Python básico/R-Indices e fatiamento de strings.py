"""Indices e fatiamento de strings
"""

#indice
#     012345 // esse aqui é o indice da string, cada numero representa um caractere da string thiago
nome="thiago"
#    -654321 // esse aqui é o indice negativo, com isso conseguimos tirar ultimos caracteres com facilidade
print(nome[:-2])    #aqui como tirar indices da string, aqui tira os 2 ultimos
print(nome[2:6])    #aqui como pegar somente do segundo caractere até o sexto
print(nome[2:])
print(nome[:]) # quando não passamos os indices ele pega o primeiro até o ultimo

#agora se a gnt quiser que leia de 2 em 2 por exemplo, é so adicionar :2
print(nome[0:6:2]) # saida foi tig
print(nome[::3]) #saida ta

# for in
for letra in nome:
    print(letra)