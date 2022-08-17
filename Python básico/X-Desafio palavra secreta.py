"""existe uma palavra secreta e o usuário deve acertar
usar lista"""

from re import T


secreta='taturana'
digitadas=[]
chances=3
while True:
    if chances<=0:
        print('você perdeu')
        break
    entrada=input('Digite uma letra:\n')
    if len(entrada)>1:
        print('digite somente uma letra')
        continue
    digitadas.append(entrada)

    if entrada in secreta:
        # print('Boa\n')
        # print(digitadas)
        ...

    else:
        # print('essa letra não existe')
        digitadas.pop()
        chances=chances-1
        # print(digitadas)
    
    temporaria=''

    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            temporaria= temporaria+letra_secreta
        else: 
            temporaria= temporaria+'*'

    if temporaria == secreta:
        print(f'Parabéns a palavra era {secreta}')
        break
    else:
        print(temporaria)
        print(f'você ainda tem {chances} chances')
    
