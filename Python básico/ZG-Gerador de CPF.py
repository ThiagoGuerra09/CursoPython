"""
Com o código anterior, criarei um gerador de CPF 
Basicamente usei uma função que pega numeros aleatorios e fiz o calculo para tornar um cpf valido
"""
from random import randint
entrada= str(randint(10000000000, 99999999999))

if not entrada.isnumeric():
    print('digite somente numeros, sem "." ou "-"')
else: 
    if not len(entrada)==11:
        print('esta faltando numero')
    else:
        contador=0 #contador para passar de letra em letra na string entrada
        acumulador=0 #acumulador que guarda os resultados das multiplicações
        for x in range(10,1,-1):
            entrada_int=int(entrada[contador])
            acumulador=acumulador+(entrada_int*x)
            contador+=1
        #primeiro digito
        result=11-(acumulador%11)
        if result>9:
            primeiro=0
        else:
            primeiro=result
        #juntando com o resto da string
        primeiro=str(primeiro)
        cpfvalidado=entrada[0:9]+primeiro
        contador=0
        acumulador=0
        for n in range(11,1,-1):
            cpfvalidadoInt=int(cpfvalidado[contador])
            acumulador=acumulador+(cpfvalidadoInt*n)
            contador+=1
        #segundo digito
        result=11-(acumulador%11)
        if result >9:
            segundo=0
        else:
            segundo=result
        #juntando o segundo digito com o resto da string
        segundo=str(segundo)
        cpfvalidado=cpfvalidado+segundo
        print(cpfvalidado)
        
