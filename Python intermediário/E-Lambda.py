"""
lambda e funções anônimas
"""
#função normal
def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)
#funções anonimas 
a = lambda x, y: x*y

print(a(2,2))

#ordenando lista forma normal

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 2]
]
def ordena(arg):
    return arg[1]

lista.sort(key=ordena, reverse=True)
print(lista)

#usando lambda
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 2]
]

lista.sort(key=lambda func: func[1], reverse = False) #key é o argumento que deve ser ordenado, reverse é se vai ser crescente ou decrescente
print(lista)

#a funçaõ sorted faz a msm coisa porem, não altera a lista original

print(sorted(lista, key=lambda i: i[1]))
