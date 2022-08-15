"""Operadores lógicos
and- se ambas condições forem atendidadas
or- se pelo menos um condição for atendidada
not- inversor de valor, caso o final da condição seria true ele retorna false por exemplo e vice versa
in- confere se o valor ta presente na variavél
not in- se naõ tiver presente na variavel

"""
#not pode ser usado para conferir se tem valor na variavél. Exemplo:
a= ''
b= 2
if not a:
    print('Digite um valor') 
if not(a==b):
    print('igual')
#in pode conferir valores em termos ou variavéis
if 'u' in 'tuta':
    print('Tem')
# not in ele entra na condição se não tiver o valor escrito
if 'u' not in 'tuta':
    print('Nao tem')