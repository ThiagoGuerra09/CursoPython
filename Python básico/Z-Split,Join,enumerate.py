"""
split - dividir uma string
join - Juntar uma lista 
enumerate enumerar elementos da lista"""

from unittest.util import sorted_list_difference


string=('Eu como abobora e as vezes, como cenoura')
listaA= string.split(' ')
palavra=''
contagem=0
for valor in listaA:
    print(f'A palavra {valor}, apareceu {string.count(valor)}x na frase.') #count() é para retornar o numero de vezes que o valor passado apareceu na lista/str passada
    qntd_de_vezes=listaA.count(valor)
    if qntd_de_vezes>contagem:
        contagem = qntd_de_vezes
        palavra=valor
print(f'A palavra {palavra} foi a que mais apareceu, com {contagem} aparições.')

""""""
string2=('   o felipe comeu pão    ')
srlimpa=string2.strip().title() #strip() remove os espaços antes e depois da string
print('////////')
print(srlimpa)

listaC=srlimpa.split(' ')#aqui tornamos a string uma lista dividida pelos espaços
print(listaC)
juntastring=' '.join(listaC)#aqui juntamos a lista para virar uma str
print(juntastring)

print('////////')
print('////////')
print('////////')
for indice, valor in enumerate(listaA):
    print(indice, valor, listaA[indice])
print('////////')

#isso que a funçaõ enumerate faz é a msm coisa que o seguinte
lista2=[[1,2], ['coc', True], ['fruta,',5]]
for indice, result in lista2:
    print(indice, result)

#desempacotamento
lista5=['arthur', 'carlos', 'bernardo']
n1, n2, n3= lista5
print(n2)#vai sair carlos