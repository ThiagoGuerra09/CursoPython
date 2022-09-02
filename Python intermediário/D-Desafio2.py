''' 1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
 função2 executada.'''

def função1(func):
    return func


def função2():
    v=19
    print (v)

função1(função2())

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""
def função1(func, *args):
    return func(*args)


def função2(valor):
    return f'ola {valor}'

def função3(valor, valor2, valor3):
    return valor, valor2, valor3

v1=função1(função2,'olerandro')
v2=função1(função3,'olivier', 'lucas', 'ton')

print(v1)
print(v2)