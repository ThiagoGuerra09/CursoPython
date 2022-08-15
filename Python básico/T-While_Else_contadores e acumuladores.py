"""contador e acumulador"""
"""contadores são utilizados para controle do loop
acumuladores são utilizados para realizar operações com os resultados obtidos do loop"""
contador=50
acumulador=0
while contador<60:
    # print(contador)
    contador+=1
    acumulador=acumulador+contador

#é possivel utilizar else no while tb, quando a condição do while for false, ele entra no else
#porem se vc usar um break e sair do loop sem ser falso, ele n vai entrar no else
else:
    print(contador)
    print(acumulador)