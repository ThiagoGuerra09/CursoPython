"""Condições
If
Elif
Else

"""
# por padrão os valores são True
if True:
    print("ola")
#o elif é como se fosse um else porém ele checa o valor como se fosse um if, logo para acessá-lo
#precisa não atender o if de cima, e sua condição passada for verdadeira.
elif False:
    print('agrr')
else: 
    print('opa')


#pode ser usado para conferir se a variavel apresenta valor
a="" #n tem valor, logo n entrou no if
if a:
    print('tem valor') 
    
    
