"""
Tuplas são listas em que os elementos não podem ser alterados
usamos os () para declarar tuplas, porem elas podem ser declaras sem tambem
"""
t1 = 1,2,3,'opa'
t2 = (1,2,3,'opa') *20


print(type(t1))
print((t2))


print(t1[0::2])#a manipulação é igual de listas 
#dessa forma alteramos para lista para alterar um elemento.
t1=list(t1)
t1[1]=5
t1=tuple(t1)
print(t1)