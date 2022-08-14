"""1-Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro."""

numero =input('Digite o numero:\n')
try:
    numero=int(numero)
    if numero%2==0:
        print(f'{numero} é par')
    else:
        print(numero,'é ímpar')
except:
    print('Não é número inteiro')

"""2-Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação aprorpiada.Ex: bom dia 0-11, boa tarde 12-17, boa noite 18-23"""

horario=input('digite a hora nesse formato exemplo "10:34":\n')
hora=horario.split(":")[0]
minuto=horario.split(':')[1]
try:
    minuto=int(minuto)
    if minuto >59:
        print("Não existe esse horário")
    else:
        try:
            hora=int(hora)
            if hora >=0 and hora<=11:
                print('bom dia')
            elif hora >=12 and hora <=17:
                print('boa tarde')
            elif hora >=18 and hora <= 23:
                print('boa noite')
            else:
                print('Não existe esse horário')
        except:
            print('Não é número')
except:
    print('Não é número')

"""3-Faça um programa que peça o primerio nome do usuário. Se o nome tiver 4 letras ou menos
escreva: 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva 'Seu nome é normal'; maior que 6 
escreva 'Seu nome é muito grande'. """

nome=input('Digite seu nome')
if nome.isnumeric():
    print('isso não é nome')
else:
    letras=len(nome)
    if letras <=4:
        print('Seu nome é curto')
    elif letras == 5 or letras == 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
       
