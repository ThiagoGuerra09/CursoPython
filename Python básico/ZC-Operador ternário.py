"""
Operador ternário 
"""
logged_user= False

if logged_user:
    msg = 'usuario logado'
else:
    msg='usuario precisa logar'

print(msg)
#para abreviar isso tudo, podemos fazer o seguinte:
logged_user= False
msg = 'usuario logado.' if logged_user else 'usuario precisa logar'
print(msg)
#exemplo 2
idade=18
if idade >=18:
    print('pode acessar')
else: 
    print('não pode acessar')
#usando operador ternário:
e_de_maior = idade>=18
msg= 'pode acessar ' if e_de_maior else 'não pode'
print(msg)
