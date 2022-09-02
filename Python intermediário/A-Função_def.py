"""Funções

"""
def função():
    print('Hello world')

função()
#se passar paramentro para função receber, deve passar um valor ao chamar a função
def função1(valor):
    valor=valor.replace('a', 'b')#substituir a por b 
    return valor #retorna o valor para onde foi chamado

armazena=função1('olaaaaa')#com o valor retornado, armazanei na "armazena"
print(armazena)

def obs(var):
    print(var)

val=obs(12)#retorna o none, que significa não valor

if val:
    print(val)
else: 
    print(val)

#como retornar uma função

def x(op):
    print(op)

def bomb():
    return x

vali=bomb()('entrei na x')#chamamos a boms, porém ela retorna outra função, com a abertura do segundo parenteses
#passei o valor para função x que printou o entrei na x 

#tuplas: é basicamente uma lista que não pode ser alterada

def funcao3():
    return 'thiago', 'guerra'

tupla=funcao3()
# tupla[0]='oi' isso é uma coisa que não acontece, visto que não pdemos atribuir novos valores pra tupla
print(tupla, type(tupla))
