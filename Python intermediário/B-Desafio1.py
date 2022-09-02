"""Desafios"""
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def saudacoes(nome, saud):
    print(f'{saud} {nome}')
saudacoes('eduardo?', 'olá, como está')

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma(x,y,z):
    print(x+y+z)
soma(1,2,3)
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def calculo(valor,porcent):
    return valor+(porcent/100*valor)
print(calculo(20,10))

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def fizbuzz(x):
    if x % 5 ==0 and x % 3 == 0:
        return 'FizzBuzz'
    elif x % 5 ==0:
        return 'buzz'
    elif x % 3 ==0:
        return 'fizz'
    else:
        return x

print(fizbuzz(7))