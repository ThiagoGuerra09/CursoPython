"""Formatando valores
:s strings
:d int
:f float
:.(Numero)f quantidade de casas decimais do float
:(caractere)(> ou < ou ^)(quantidade)(tipo-s,d, ou f)

> esquerda
< direita
^ centro
"""
n1=10
n2=3
div=n1/n2
print(f'{div:.2f}')

print(f'{n1:0>10.2f}')
print(f'{n1:0<10}')
print(f'{n1:0^10}')

print(f'{n1:%^6}')

nome='thiago'
sobrenome='guerra'
nomeformatado= '{0:$>50}{1:@<34}'.format(nome, sobrenome)
print(nomeformatado)
#outras funções
#ljust() adiciona no final o tanto de caractere que você quer de tal caractere
#lower() poe todas as letras em minusculo
#upper() poe todos em maiusculo
#title() poe as primeiras letras em maiusculo
nome= 'tHI'
# nome= nome.ljust(20, '%')
# nome= nome.lower()
# nome= nome.upper()
nome= nome.title()
print(nome)



