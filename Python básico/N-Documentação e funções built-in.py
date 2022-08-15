"""Documentação
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""

"""Funções
isdigit(), isdecimal(), isnumeric()
Essas funções estão presentes na documentação acima
"""

n1=input('digite um numero')
n2=input('digite um numero')

if(n1.isdigit() and n2.isdigit()):
    print(n1 + n2)
else:
    print('você não digitou numeros')

#try and except: como se fosse um if else, a gnt pede pra ele tentar executr um bloco de código e se n 
# der certo, ele entra no except, porem ele n confere condição para entrar, ele já sai entrando no bloco

n1=input('digite um numero')
n2=input('digite um numero')

try:
    (n1.isdigit() and n2.isdigit())
    print(n1 + n2)
except:
    print('você não digitou numeros')