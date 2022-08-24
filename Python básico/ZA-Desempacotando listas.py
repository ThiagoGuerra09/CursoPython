"""
Desempacotamento de lista
"""
lista = ['Luiz', 'joca', 'Maria', 1, 2,3,4,5]

n1, n2, *outralista, n3= lista #no n1 e n2 é atribuido variavies e no *outralista, é atribuido outra lista para os valores remanescentes
#n3 é o ultimo valor, no caso o 5
print(outralista)#aqui sai ['Maria', 1, 2, 3, 4]