"""Listas em Python
fatimento
append, insert, pop, del, clear, extend, +
min, max
range"""

#lista é como se fosse uma variavel com varios valores dentro dela
#indice 0  1    2     3     4
lista= [1, 2, "thi", True, 'd' ]
#i.neg -5  -4   -3    -2    -1

print(lista[-1])#acessando o indice -1 ou 4 da lista
#supondo que eu queira mudar um valor da lista
lista[4]=5 #trocou o valor d pelo valor 5
print(lista)
#printar um pedaço
print(lista[0:3:1])
print(lista[:3])
print(lista[0::2])
#inverter a lista
print(lista[::-1])#começa do 0 e vai dando -1, logo vai printando pelo indice negativo a lista de trás pra frente
#usando funções na lista
print('/')
l1= [1,2,3]
l2= [4,5,6]
l3= l1 +l2 #criamos uma nova lista que concatenou o valor de duas listas
print(l3)
#porem se eu não quiser criar uma nova lista para concatenar, eu posso extender uma lista usando a função extend()
l1.extend(l2)
print(l1)
l1.extend('opa') #ao inserir assim, separou cada letra em um indice
print(l1)
#adicionar um novo valor no final lista append()
l2.append('opa') #ao inserir assim, a string inteira ficou em somente um indice
print(l2)
#para você adicionar onde você quiser usar função insert()
l2.insert(2, 'banana') #detalhe, ele n substitui o valor anterior, ele pula um indice para adicionar
print(l2)
#para remover um valor no final da lista funçaõ pop()
l2.pop()
print(l2)
#para remover onde você quiser usamos a função del()
del(l2[2])
print(l2)
del(l2[:1])
print(l2)
#para pegar o valor maximo e minimo da lista, funções max() e min()
print(max(l2))
print(min(l2))
#para usar um range com uma lista usamos a função list()
l2= list(range(0,100,8)) #a list transforma um objeto iteravel no caso o range em uma lista.
print(l2)
l3= range(0,100,8) #aqui vemos que o objeto não vira uma lista sozinho, precisa da fução lista
print(l3)
# podemos usar o for para manipular valores de uma lista também

soma=0
for valor in l2:
    soma+=valor #soma= soma + valor(acumulador)
print(soma)
# para a gnt pegar o tipo de elemento de cada valor funçaõ type()
lista= [1, 2, "thi", True, 'd' ]

for elemento in lista:
    print(f'O elemento {elemento} é do tipo {type(elemento)}')
